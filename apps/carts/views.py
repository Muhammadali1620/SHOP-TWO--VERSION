from django.shortcuts import render, redirect
from apps.carts.models import Cart
from apps.features.models import ProductFeature
from django.db.models import Sum, Count
from django.contrib import messages
from apps.general.models import Coupon
from django.contrib.auth.decorators import login_required


@login_required
def add_to_cart(request, pk):
    user = request.user
    counts = request.POST.get('counts', 1)
    features = [int(request.POST[feature]) for feature in request.POST if feature.startswith('feature_')]

    product_feaatures = ProductFeature.objects.annotate(count=Count('feature_value')).filter(product_id=pk, count=len(features))

    for feature_value_id in features:
        product_feaatures = product_feaatures.filter(feature_value__id=feature_value_id)
    if product_feaatures:
        user_cart, created = Cart.objects.get_or_create(productfeature_id=product_feaatures.first().pk, user_id=user.pk)
        if created:
            user_cart.counts = int(counts)
            user_cart.save()
            messages.success(request, 'sucsessfuly added to cart')
        else:
            messages.error(request, 'this product already to your cart')

    else:
        messages.error(request, 'product feature does not exst')
    return redirect('product-detail', pk=pk)


@login_required
def delete_cart(request, pk):
    obj = Cart.objects.get(pk=pk)
    if obj:
        obj.delete()
    return redirect('cart_page')


@login_required
def cart_page(request):
    user = request.user
    carts = Cart.objects.filter(user_id=user.pk).select_related('productfeature')
    price = carts.values('productfeature__price', 'counts')
    subtotal = []
    for i in price:
        result = i['productfeature__price'] * i['counts']
        subtotal.append(result)
    context = {
        'carts':carts,
        'subtotal':sum(subtotal),
    }
    #coupon
    coupon_code = request.POST.get('coupon_code')
    if coupon_code:
        coupon = Coupon.check_coupon(code=coupon_code, request=request)
        if coupon:
            request.session['amount'] = int(coupon[0])
            request.session['is_percent'] = coupon[1]
            request.session['code'] = coupon_code            
            messages.success(request, 'Your coupon is activate')
            if coupon[1]:
                subamount = sum(subtotal) / 100 * coupon[0]
            else:
                subamount = sum(subtotal) - coupon[0]
            request.session['subamount'] = int(subamount)
        else:
            messages.error(request, 'Copon code is not valid!')
    return render(request, template_name='cart.html', context=context)


@login_required
def update_count(request, pk):
    if request.method != 'POST':
        return redirect('cart_page')
    counts = request.POST.get('counts')

    cart = Cart.objects.get(pk=pk)
    quant = cart.productfeature.quantity

    if int(counts) > quant:
        messages.error(request, f'{quant}-limit product')
    else:
        cart.counts = counts
        cart.save()
        messages.success(request, 'OK')

    return redirect('cart_page')