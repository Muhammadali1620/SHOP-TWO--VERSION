from django import forms
from apps.features.models import FeatureValue
from apps.products.models import Product
from apps.categories.models import SubCategory


class ProductForm(forms.ModelForm):
    sub_category = forms.ModelChoiceField(queryset=SubCategory.objects.all().select_related('main_category'))
    class Meta:
        model = Product
        fields = '__all__'

class ProductFeatureForm(forms.ModelForm):
    feature_value = forms.ModelMultipleChoiceField(queryset=FeatureValue.objects.all().select_related('feature'))
    class Meta:
        model = Product
        fields = '__all__'
