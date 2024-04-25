from typing import Any
from django.contrib import admin
from apps.users.models import CustomUser
from django.contrib.auth.models import Group
from rangefilter.filters import DateRangeFilterBuilder


admin.site.unregister(Group)


@admin.register(CustomUser) 
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone_number')
    list_display_linsk = ('email', 'first_name', 'last_name', 'phone_number')
    list_filter = (('date_joined', DateRangeFilterBuilder(),),)
    ordering = ('-date_joined',)
    search_fields = ['email', 'first_name', 'last_name', 'phone_number']
    search_help_text = f'Serch from fields({search_fields})'
    readonly_fields = ['last_login', 'email', 'date_joined',]
    fields = ['last_login', 'is_active', 'date_joined', 'email', 'password',
              'first_name', 'last_name', 'phone_number', 'address1', 'address2',
              'country', 'region', 'district', 'zip_code']

    def save_model(self, request, obj, form, change):
        if obj.pk and CustomUser.objects.get(pk=obj.pk).password != obj.password:
            obj.set_password(obj.password)
        obj.save()

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(is_staff=False)

    def has_add_permission(self, request):
        return False
