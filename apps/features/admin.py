from django.contrib import admin
from apps.features.models import Feature, FeatureValue


class FeatureValueInlineAdmin(admin.StackedInline):
    model = FeatureValue
    min_num = 1 


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('main_category', 'sub_category', 'name_uz', 'name_ru')
    readonly_fields = ('created_at','updated_at',)
    prepopulated_fields = {'slug':['name_uz']}
    list_display_linsk = ('main_category', 'sub_category')
    list_filter = ['main_category','sub_category']
    search_fields = ['name_uz', 'name_ru']
    search_help_text = f'Serch from fields({search_fields})'
    list_editable = ['name_uz', 'name_ru']
    inlines = [FeatureValueInlineAdmin]