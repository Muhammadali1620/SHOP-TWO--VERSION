from apps.products.views import product_list, product_detail
from django.urls import path


urlpatterns = [
    path('', product_list, name='product-list' ), 
    path('detail/<int:pk>', product_detail, name='product-detail' ), 
]