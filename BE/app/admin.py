from django.contrib import admin
from .models import Order, Nansu, OrderInfo, Calendar, Image, JanFront, JanBack, FebFront, FebBack, MarFront, MarBack, AprilFront, AprilBack, MayFront, MayBack, JuneFront, JuneBack, JulyFront, JulyBack, AugFront, AugBack, SepFront, SepBack, OctFront, OctBack, NovFront, NovBack, DecFront, DecBack, Prolog, Cover
from .forms import OrderForm
from django.utils.timezone import now
import random

#admin.site.register(Order)
admin.site.register(OrderInfo)
admin.site.register(Calendar)
admin.site.register(Image)
admin.site.register(JanFront)
admin.site.register(JanBack)
admin.site.register(FebFront)
admin.site.register(FebBack)
admin.site.register(MarFront)
admin.site.register(MarBack)
admin.site.register(AprilFront)
admin.site.register(AprilBack)
admin.site.register(MayFront)
admin.site.register(MayBack)
admin.site.register(JuneFront)
admin.site.register(JuneBack)
admin.site.register(JulyFront)
admin.site.register(JulyBack)
admin.site.register(AugFront)
admin.site.register(AugBack)
admin.site.register(SepFront)
admin.site.register(SepBack)
admin.site.register(OctFront)
admin.site.register(OctBack)
admin.site.register(NovFront)
admin.site.register(NovBack)
admin.site.register(DecFront)
admin.site.register(DecBack)
admin.site.register(Prolog)
admin.site.register(Cover)


class OrderAdmin(admin.ModelAdmin):
    form = OrderForm
    
admin.site.register(Order, OrderAdmin)

# admin.site.register(Order, OrderAdmin)
class NansuAdmin(admin.ModelAdmin): #난수 생성 액션
    actions = ['insert_random_nansu','update_date_field']

    def insert_random_nansu(self, request, queryset):
        for obj in queryset:
            obj.nansu = str(random.randint(10**(8-1), (10**8)-1))
            obj.save()
        self.message_user(request, f"{queryset.count()} 개의 난수가 생성 되었습니다.")
    insert_random_nansu.short_description = "난수 생성"

    def update_date_field(self, request, queryset):
        updated_count = queryset.update(created_at=now().date())
        self.message_user(request, f"{queryset.count} 개의 날짜 정보가 등록 되었습니다.")
    update_date_field.short_description="날짜 생성 액션(필수)"

admin.site.register(Nansu, NansuAdmin)

