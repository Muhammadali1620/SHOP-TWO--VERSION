from django.shortcuts import render, redirect
from apps.categories.models import MainCategory
from apps.features.models import Feature
from django.db.models import F, Q
from apps.products.models import Product
from math import ceil
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from apps.wishlists.models import Wishlist


def product_list(request):
    feature_values = request.GET.getlist('feature_values')
    select_sub_cat_id = request.GET.get('sub_category', '0')
    query = request.GET.get('query', '')
    products = Product.objects.all().order_by('-pk')
    if query != '':
        request.session['query'] = query
    else:
        request.session['query'] = ''
    if request.session.get('query'):
        products = products.filter(Q(title_uz__icontains=query) |
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
        select_sub = request.session['select_sub_cat_id']
        main = get_object_or_404(MainCategory, sub_cat__id=select_sub)
        features = Feature.objects.filter(main_category_id=main.pk).order_by('ordering_number')[:5].prefetch_related('values')
        products = products.filter(sub_category_id=select_sub)
    else:
        features = Feature.objects.all().order_by('ordering_number')[:5].prefetch_related('values')
    
    if feature_values:
        products = products.filter(product_features__feature_value__id__in=feature_values).distinct()

    paginator = Paginator(products, 9)
    number_page = request.GET.get('page', '1')
    page_obj = paginator.get_page(number_page)
    context={
        'page_obj':page_obj,
        'features':features,
        'feature_values':list(map(int, feature_values))
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