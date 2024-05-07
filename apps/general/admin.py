from django.contrib import admin
from django.http import HttpRequest
from apps.general.models import SocialLink, PaymentMethod, General, Service, Branch, Banner, Coupon

 
@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('slug','name', 'link')
    prepopulated_fields = {'slug':['name']}
    readonly_fields = ('created_at','updated_at',)
    list_display_linsk = ('slug')
    search_fields = ['name', 'link']
    search_help_text = f'Serch from fields({search_fields})'
    list_editable = ['name', 'link']


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('slug','name')
    prepopulated_fields = {'slug':['name']}
    readonly_fields = ('created_at',)
    list_display_linsk = ('slug')
    search_fields = ['slug','name']
    search_help_text = f'Serch from fields({search_fields})'
    list_editable = ['name']


@admin.register(General)
class GeneralAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'email',)
    readonly_fields = ('created_at','updated_at')
    list_display_linsk = ('phone_number', 'email')

    def has_add_permission(self, request):
        return not General.objects.exists()


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('slug','title_uz', 'title_ru')
    prepopulated_fields = {'slug':['title_uz']}
    readonly_fields = ('created_at','updated_at',)
    list_display_linsk = ('slug')
    search_fields = ['slug','title_uz', 'title_ru']
    search_help_text = f'Serch from fields({search_fields})'
    list_editable = ['title_uz', 'title_ru']


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title_uz', 'title_ru')
    prepopulated_fields = {'slug':['title_uz']}
    readonly_fields = ('created_at','updated_at',)
    list_display_linsk = ('slug')
    search_fields = ['slug', 'title_uz', 'title_ru']
    search_help_text = f'Serch from fields({search_fields})'
    list_editable = ['title_uz', 'title_ru']


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('sub_category', 'title_uz', 'title_ru')
    prepopulated_fields = {'slug':['title_uz']}
    readonly_fields = ('created_at','updated_at',)
    list_display_linsk = ('sub_category')
    #list_filter = ['sub_category']
    search_fields = ['title_uz', 'title_ru']
    search_help_text = f'Serch from fields({search_fields})'
    list_editable = ['title_uz', 'title_ru']


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'amount', 'amount_is_percent')
    readonly_fields = ('created_at','updated_at',)
    list_display_linsk = ('code')
    search_fields = ['code', 'title', 'amount', 'amount_is_percent']
    search_help_text = f'Serch from fields({search_fields})'
    list_editable = ['title', 'amount', 'amount_is_percent']