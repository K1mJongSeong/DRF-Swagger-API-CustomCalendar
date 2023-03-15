from .models import Order
from django import forms

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'orderState': forms.Select(choices=Order.ORDER_STATE_CHOICES),
        }