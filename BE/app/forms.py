from .models import Order
from django import forms

class OrderForm(forms.ModelForm):
    order_date = forms.DateTimeField(input_formats=['%Y-%m-%dT%H:%M:%S'], widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'orderState': forms.Select(choices=Order.ORDER_STATE_CHOICES),
            # 'order_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M:%S'),
        }
