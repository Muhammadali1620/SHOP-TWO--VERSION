from django.shortcuts import render
from apps.features.models import Feature
from django.db.models import F, Q
from apps.products.models import Product


def product_list(request):
    select_sub_cat_id = request.GET.get('sub_category', '0')
    query = request.GET.get('query', '')
    page = request.GET.get('page')
    if page == None:
        page = 1
    d = int(page) * 9 
    limit = 0 + d
    ofset = -9 + d
    products = Product.objects.all().order_by('-pk')[ofset:limit]
    if str(select_sub_cat_id).isdigit():
        select_sub_cat_id = int(select_sub_cat_id)
        if select_sub_cat_id != 0:
            request.session['select_sub_cat_id'] = select_sub_cat_id
        else:
            if request.session.get('select_sub_cat_id'):
                del request.session['select_sub_cat_id']
    if request.session.get('select_sub_cat_id'):
        features = Feature.objects.filter(sub_category_id=request.session['select_sub_cat_id'])
        products = Product.objects.filter(sub_category_id=request.session['select_sub_cat_id'])[:9]
        #feature = Feature.objects.annotate(F)
    else:
        features = Feature.objects.all().order_by('-pk')[:5]
    if query:
        request.session['query'] = query

    context={
        'products':products,
        'features':features,
        'page':int(page)
    }
    return render(request, template_name='products/product_list.html', context=context)
