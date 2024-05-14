from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from apps.orders.models import Order, OrderProduct


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'payment_method', 'total_price', 'delivery_price', 'coupon_price', 'is_paid',
                    'email', 'phone_number',)
    readonly_fields = ('created_at',)

    list_display_linsk = ('user', 'payment_method', 'total_price', 'delivery_price', 'coupon_price', 'is_paid',
                    'email', 'phone_number',)
    search_fields = ['total_price', 'delivery_price', 'coupon_price', 'email', 'phone_number']
    search_help_text = f'Serch from fields({search_fields})'
    list_select_related = ['user', 'payment_method']

    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request: HttpRequest, obj: Any | None = ...) :
        return False
    
    def has_delete_permission(self, request: HttpRequest, obj: Any | None = ...):
        return False



@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('product_feature', 'counts', 'order')
    readonly_fields = ('created_at',)

    list_display_linsk = ('product_feature', 'order')
    search_fields = ['counts']
    search_help_text = f'Serch from fields({search_fields})'
    list_editable = ['counts']
    list_select_related = ['order', 'order__user', 'product_feature', 'product_feature__product']


    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request: HttpRequest, obj: Any | None = ...) :
        return False
    
    def has_delete_permission(self, request: HttpRequest, obj: Any | None = ...):
        return False