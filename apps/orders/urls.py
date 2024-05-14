from django.urls import path
from apps.orders.views import check_page, order


urlpatterns = [
    path('check/', check_page, name='check_page'),
    path('order/', order, name='order'),
]