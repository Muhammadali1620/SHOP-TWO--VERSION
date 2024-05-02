from apps.products.views import product_list, product_detail, product_wishlist, wishlist
from django.urls import path


urlpatterns = [
    path('', product_list, name='product-list' ), 
    path('detail/<int:pk>', product_detail, name='product-detail' ),
    path('creat-wishlist/<int:pk>', product_wishlist, name='product-wishlist' ),
    path('wishlist/', wishlist, name='wishlist' ),
]