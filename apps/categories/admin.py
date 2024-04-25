from django.contrib import admin
from apps.categories.models import MainCategory, SubCategory


class SubCategoryInline(admin.StackedInline):
    model = SubCategory
    verbose_name = 'Sub Categories' 
    extra = 3
    prepopulated_fields = {'slug':['name_uz']}


@admin.register(MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name_uz', 'name_ru')
    readonly_fields = ('created_at','updated_at')
    prepopulated_fields = {'slug':['name_uz']}
    inlines = [SubCategoryInline]
    list_display_linsk = ('pk')
    search_fields = ['name_uz','name_ru']
    search_help_text = f'Serch from fields({search_fields})'
    list_editable = ['name_uz', 'name_ru']