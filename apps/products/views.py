from django.shortcuts import get_object_or_404, render
from apps.features.models import Feature, FeatureValue, ProductFeature
from apps.products.models import Product
from apps.general.models import General
from apps.categories.models import MainCategory, SubCategory
from django.db.models import F


def product_list(request):
    return render(request, template_name='products/product_list.html')
