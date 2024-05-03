from django.shortcuts import render
from apps.categories.models import MainCategory
from apps.general.models import General
from apps.products.models import Product



def home(request):
    featured_products = Product.objects.all().order_by('?')[:8].prefetch_related('image_product')
    recent_products = Product.objects.all().order_by('?')[:8].prefetch_related('image_product')
    context = {
        'featured_products':featured_products,
        'recent_products':recent_products
    }
    return render(request, template_name='index.html', context=context)