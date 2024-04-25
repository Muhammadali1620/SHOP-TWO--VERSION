from apps.products.views import product_list
from django.urls import path


urlpatterns = [
    path('', product_list, name='product-list' ), 
]