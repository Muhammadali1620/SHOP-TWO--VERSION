from django.shortcuts import redirect, render
from apps.categories.models import MainCategory
from apps.general.models import Banner, Branch, Coupon, General, Service
from apps.products.models import Product



def home(request):
    featured_products = Product.objects.all().order_by('?')[:8].prefetch_related('image_product')
    recent_products = Product.objects.all().order_by('-created_at')[:8].prefetch_related('image_product')
    branchs = Branch.objects.all()[:6]
    services = Service.objects.all()[:4]
    banners = Banner.objects.all()[:3]
    banners_two = Banner.objects.all()[4:6]
    banners_three = Banner.objects.all()[6:8]
    context = {
        'featured_products':featured_products,
        'recent_products':recent_products,
        'branchs':branchs,
        'services':services,
        'banners':banners,
        'banners_two':banners_two,
        'banners_three':banners_three,
    }
    return render(request, template_name='index.html', context=context)  