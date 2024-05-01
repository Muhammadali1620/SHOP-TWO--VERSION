from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from apps.contacts.models import Contact

 
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    readonly_fields = ('created_at',)

    list_display_linsk = ('email', 'title', 'message')
    search_fields = ('email', 'title', 'message')
    search_help_text = f'Serch from fields({search_fields})'

    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request: HttpRequest, obj: Any | None = ...) :
        return False
    
    def has_delete_permission(self, request: HttpRequest, obj: Any | None = ...):
        return False