from django.shortcuts import render, redirect
from apps.carts.models import Cart
from django.contrib.auth.decorators import login_required
from apps.features.models import ProductFeature
from apps.general.models import General
from apps.orders.forms import OrderCreateForm
from django.contrib import messages

from apps.orders.models import OrderProduct



@login_required
def check_page(request):
    user = request.user
    shipping = 0
    carts = Cart.objects.filter(user=user.pk)
    price = carts.values('productfeature__price', 'counts')
    obj = General.objects.first()
    if not obj:
        shipping = 0
    else:
        shipping = obj.shipping
    subtotal = []
    for i in price:
        result = i['productfeature__price'] * i['counts']
        subtotal.append(result)
    context = {
        'carts':carts,
        'subtotal':sum(subtotal),
        'shipping':int(shipping)
    }
    return render(request, template_name='checkout.html', context=context)

@login_required
def order(request):
    if request.method != 'POST':
        return redirect('check_page')
    user = request.user
    carts = Cart.objects.filter(user_id=user.pk)
    form = OrderCreateForm(request.POST)
    if not form.is_valid():
        messages.error(request, form.errors)
        return redirect('check_page')
    
    obj = form.save()
    for cart in carts:
        order_poduct = OrderProduct(product_feature_id=cart.productfeature.pk, counts=cart.counts, order=obj)
        if order_poduct:
            order_poduct.save()
        else:
            messages.success(request, 'Something went wrong, try again!')
            return redirect('check_page')
    messages.success(request, 'Your order was succsesfully created.')       
    request.session['amount'] = ''
    request.session['is_percent'] = ''
    request.session['subamount'] = ''
    request.session['code'] = '' 
    return redirect('check_page')