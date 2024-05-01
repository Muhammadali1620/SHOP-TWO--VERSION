from django.contrib import admin
from apps.features.models import ProductFeature
from apps.products.models import Product, ProductImage


class ProductImageInlineAdmin(admin.TabularInline):
    model = ProductImage
    min_num = 1
    max_num = 10
    extra=2


class ProductFeatureInline(admin.TabularInline):
    model = ProductFeature
    min_num = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title_uz', 'title_ru', 'rating')
    readonly_fields = ('created_at','updated_at','rating','review_counts')
    prepopulated_fields = {'slug':['title_uz']}

    list_display_linsk = ('slug')
    list_filter = ['rating']
    search_fields = ['title_uz', 'title_ru', 'review_counts']
    search_help_text = f'Serch from fields({search_fields})'
    list_editable = ['title_uz', 'title_ru',]
    inlines = [ProductImageInlineAdmin, ProductFeatureInline]