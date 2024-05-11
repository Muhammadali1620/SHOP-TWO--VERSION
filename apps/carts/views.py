from django.shortcuts import render, redirect
from apps.carts.models import Cart
from apps.features.models import ProductFeature
from django.db.models import Sum
from django.contrib import messages
from apps.general.models import Coupon


def add_to_cart(request, pk):
    user = request.user
    if not user.is_authenticated:
        return redirect('login_page')
    counts = request.POST.get('counts', 1)
    features = [int(request.POST[feature]) for feature in request.POST if feature.startswith('feature_')]
    product_feaature = ProductFeature.objects.filter(product_id=pk, feature_value__id__in=features).first()
    if product_feaature:
        Cart.objects.create(productfeature_id=product_feaature.pk, user_id=user.pk, counts=int(counts))
    return redirect(request.META['HTTP_REFERER'])


def delete_cart(request, pk):
    user = request.user
    if not user.is_authenticated:
        return redirect('login_page')
    obj = Cart.objects.get(pk=pk)
    if obj:
        obj.delete()
    return redirect('cart_page')


def cart_page(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('login_page')
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
            messages.success(request, 'Your coupon is activate')
            if coupon[1]:
                subamount = sum(subtotal) / 100 * coupon[0]
            else:
                subamount = sum(subtotal) - coupon[0]
            request.session['subamount'] = int(subamount)
        else:
            messages.error(request, 'Copon code is not valid!')
    return render(request, template_name='cart.html', context=context)