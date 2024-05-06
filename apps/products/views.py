from django.shortcuts import render, redirect
from apps.features.models import Feature
from django.db.models import F, Q
from apps.products.models import Product
from math import ceil
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

from apps.wishlists.models import Wishlist


def product_list(request):
    # c = Product.objects.count() / 9
    # end_page = False
    # plus = 1
    # minus = 1
    # if int(page) >= ceil(c):
    #     end_page = True
    #     plus = 0
    # if int(page) <= 1:
    #     minus = 0
    # d = int(page) * 9 
    # limit = 0 + d
    # ofset = -9 + d    
    select_sub_cat_id = request.GET.get('sub_category', '0')
    query = request.GET.get('query', '')
    products = Product.objects.all().order_by('-pk')
    if query != '':
        request.session['query'] = query
    if request.session.get('query'):
        products = Product.objects.filter(Q(title_uz__icontains=query) |
                                          Q(title_ru__icontains=query) |
                                          Q(short_desc_uz__icontains=query) |
                                          Q(short_desc_ru__icontains=query) |
                                          Q(long_desc_uz__icontains=query) |
                                          Q(long_desc_ru__icontains=query))
    if str(select_sub_cat_id).isdigit():
        select_sub_cat_id = int(select_sub_cat_id)
        if select_sub_cat_id != 0:
            request.session['select_sub_cat_id'] = select_sub_cat_id
        else:
            if request.session.get('select_sub_cat_id'):
                del request.session['select_sub_cat_id']
    if request.session.get('select_sub_cat_id'):
        features = Feature.objects.filter(sub_category_id=request.session['select_sub_cat_id'])[:5].prefetch_related('values')
        products = Product.objects.filter(sub_category_id=request.session['select_sub_cat_id'])
    else:
        features = Feature.objects.all().order_by('-pk')[:5].prefetch_related('values')

    paginator = Paginator(products, 9)
    number_page = request.GET.get('page', '1')
    page_obj = paginator.get_page(number_page)
    context={
        'page_obj':page_obj,
        'features':features,
        # 'previouse':int(page) - minus,
        # 'next':int(page) + plus,
        # 'end_page':end_page
    }
    return render(request, template_name='products/product_list.html', context=context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product':product
    } 
    return render(request, template_name='products/product_detail.html', context=context)


def product_wishlist(request, pk):
    user = request.user
    if not user.is_authenticated:
        return redirect('login_page')
    obj, created = Wishlist.objects.get_or_create(user_id=user.pk, product_id=pk)
    if not  created:
        obj.delete()
    return redirect(request.META['HTTP_REFERER'])


def wishlist(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('login_page')
    products = Wishlist.objects.filter(user_id=user.pk).order_by('-pk')
    paginator = Paginator(products, 9)
    number_page = request.GET.get('page', '1')
    page_obj = paginator.get_page(number_page)
    context = {
        'page_obj':page_obj
    }
    return render(request, template_name='products/product_wishlist.html', context=context)