from django.urls import path
from apps.carts.views import add_to_cart, cart_page, delete_cart, update_count


urlpatterns = [
    path('add/<int:pk>/', add_to_cart, name='add_to_cart'),
    path('', cart_page, name='cart_page'),
    path('delete/<int:pk>', delete_cart, name='delete_cart'),
    path('update_count/<int:pk>', update_count, name='update_count'),
]