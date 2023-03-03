from django.contrib import admin
from .models import Order, Nansu, OrderInfo, Calendar, Image


admin.site.register(Order)
admin.site.register(OrderInfo)
admin.site.register(Nansu)
admin.site.register(Calendar)
admin.site.register(Image)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('user', 'product', 'quantity',)

# admin.site.register(Order, OrderAdmin)