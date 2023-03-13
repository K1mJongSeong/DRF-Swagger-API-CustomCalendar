from django.contrib import admin
from .models import Order, Nansu, OrderInfo, Calendar, Image
from django.utils.timezone import now
import random

admin.site.register(Order)
admin.site.register(OrderInfo)
#admin.site.register(Nansu)
admin.site.register(Calendar)
admin.site.register(Image)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('user', 'product', 'quantity',)

# admin.site.register(Order, OrderAdmin)
class NansuAdmin(admin.ModelAdmin): #난수 생성 액션
    actions = ['insert_random_nansu','update_date_field']

    def insert_random_nansu(self, request, queryset):
        for obj in queryset:
            obj.nansu = str(random.randint(10**(8-1), (10**8)-1))
            obj.save()
        self.message_user(request, f"{queryset.count()} items have been inserted.")
    insert_random_nansu.short_description = "난수 생성"

    def update_date_field(self, request, queryset):
        updated_count = queryset.update(created_at=now().date())
        self.message_user(request, f"{queryset.count} 가 등록 되었습니다.")
    update_date_field.short_description="날짜 생성 액션(필수)"

admin.site.register(Nansu, NansuAdmin)

