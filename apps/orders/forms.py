from django import forms
from apps.orders.models import Order, OrderProduct


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
