from django.shortcuts import render, redirect
from apps.carts.models import Cart
from apps.features.models import ProductFeature
from django.db.models import Sum

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
    return render(request, template_name='cart.html', context=context)