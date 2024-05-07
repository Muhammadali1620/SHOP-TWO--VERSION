from django import forms
from apps.products.models import Product
from apps.categories.models import SubCategory
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    sub_category = forms.ModelChoiceField(required=False, queryset=SubCategory.objects.all().select_related('main_category'))
    class Meta:
        model = Product
        fields = '__all__'

        def clean(self):
            product = self.cleaned_data['product']
            feature_values = self.cleaned_data['feature_value', []]

            for feture_value in feature_values:
                if feture_value.feature.main_category != product.main_category:
                    raise ValidationError({'feature_value':'category errror'})

            return self.cleaned_data