from django.urls import path
from apps.orders.views import check_page 


urlpatterns = [
    path('check/', check_page, name='check_page'),
]