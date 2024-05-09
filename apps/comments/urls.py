from apps.comments.views import add_comment
from django.urls import path


urlpatterns = [
    path('add/<int:pk>/', add_comment, name='add_comment' ), 
]