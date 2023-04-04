from .models import Order, Notice
#from django.contrib.auth.forms import UserChangeForm, UserCreationForm
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
        labels = {
            'order_date': '주문 날짜',
        }

class NoticeForm(forms.ModelForm):
    monthdays = forms.DateTimeField(input_formats=['%Y-%m-%dT%H:%M:%S'], widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Notice
        fields = '__all__'


# class CustomUserChangeForm(UserChangeForm):
#     class Meta(UserChangeForm.Meta):
#         model = CustomUser


# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = CustomUser