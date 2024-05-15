from django import forms
from apps.users.models import CustomUser


class CustomUserCreateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone_number', 'address1', 'address2', 'state', 'region', 'zip_code')