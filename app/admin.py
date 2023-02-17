from django.contrib import admin
from .models import MyModel
from .models import Order


admin.site.register(MyModel)
admin.site.register(Order)

# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('user', 'product', 'quantity',)

# admin.site.register(Order, OrderAdmin)