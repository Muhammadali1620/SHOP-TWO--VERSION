from django.shortcuts import render, redirect
from apps.carts.models import Cart


def check_page(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('login_page')
    carts = Cart.objects.filter(user=user.pk)
    price = carts.values('productfeature__price', 'counts')
    subtotal = []
    for i in price:
        result = i['productfeature__price'] * i['counts']
        subtotal.append(result)
    context = {
        'carts':carts,
        'subtotal':sum(subtotal)
    }
    return render(request, template_name='checkout.html', context=context)


def order_page(request):
    request.session['amount'] = ''
    request.session['is_percent'] = ''
    request.session['subamount'] = ''
    return redirect(request.META['HTTP_REFERER'])