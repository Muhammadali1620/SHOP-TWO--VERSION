from django.shortcuts import render
from apps.categories.models import MainCategory
from apps.general.models import General
from apps.products.models import Product



def home(request): 
    return render(request, template_name='index.html')