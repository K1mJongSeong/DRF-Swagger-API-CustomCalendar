from django.contrib import admin
from .models import Order, Nansu, OrderInfo, Calendar


admin.site.register(Order)
admin.site.register(OrderInfo)
admin.site.register(Nansu)
admin.site.register(Calendar)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('user', 'product', 'quantity',)

# admin.site.register(Order, OrderAdmin)