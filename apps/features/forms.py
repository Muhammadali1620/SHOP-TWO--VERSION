from django import forms
from apps.features.models import Feature, FeatureValue, ProductFeature
from apps.categories.models import SubCategory


class ProductFeatureForm(forms.ModelForm):
    feature_value = forms.ModelMultipleChoiceField(queryset=FeatureValue.objects.all().select_related('feature'))
    class Meta:
        model = ProductFeature
        fields = '__all__'


class FeatureForm(forms.ModelForm):
    values = forms.ModelMultipleChoiceField(required=False, queryset=FeatureValue.objects.all().select_related('feature'))
    sub_category = forms.ModelChoiceField(required=False, queryset=SubCategory.objects.all().select_related('main_category'))
    class Meta:
        model = Feature
        fields = '__all__'