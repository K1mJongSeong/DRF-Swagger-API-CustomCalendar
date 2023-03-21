from .models import Order, Notice
from django import forms

class OrderForm(forms.ModelForm):
    order_date = forms.DateTimeField(input_formats=['%Y-%m-%dT%H:%M:%S'], widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'orderState': forms.Select(choices=Order.ORDER_STATE_CHOICES),#드롭다운 메뉴
            # 'order_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M:%S'),
        }

class NoticeForm(forms.ModelForm):
    monthdays = forms.DateTimeField(input_formats=['%Y-%m-%dT%H:%M:%S'], widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Notice
        fields = '__all__'