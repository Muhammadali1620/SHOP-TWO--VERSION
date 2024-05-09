from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from apps.carts.models import Cart


@admin.register(Cart) 
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'productfeature', 'counts')
    search_fields = ['counts']
    search_help_text = f'Serch from fields({search_fields})'

    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request: HttpRequest, obj: Any | None = ...) :
        return False
