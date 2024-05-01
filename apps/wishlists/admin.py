from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from apps.wishlists.models import Wishlist


@admin.register(Wishlist) 
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created_at')
    readonly_fields = ('created_at',)

    list_display_linsk = ('user', 'product', 'created_at')

    # def has_add_permission(self, request):
    #     return False
    
    # def has_change_permission(self, request: HttpRequest, obj: Any | None = ...) :
    #     return False
    
    # def has_delete_permission(self, request: HttpRequest, obj: Any | None = ...):
    #     return False