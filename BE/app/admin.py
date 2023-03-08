from django.contrib import admin
from .models import Order, Nansu, OrderInfo, Calendar, Image
import random

admin.site.register(Order)
admin.site.register(OrderInfo)
#admin.site.register(Nansu)
admin.site.register(Calendar)
admin.site.register(Image)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('user', 'product', 'quantity',)

# admin.site.register(Order, OrderAdmin)
class NansuAdmin(admin.ModelAdmin):
    actions = ['insert_random_nansu']

    def insert_random_nansu(self, request, queryset):
        for obj in queryset:
            obj.nansu = str(random.randint(10**(10-1), (10**10)-1))
            obj.save()
        self.message_user(request, f"{queryset.count()} items have been inserted.")
    insert_random_nansu.short_description = "난수 생성"

admin.site.register(Nansu, NansuAdmin)