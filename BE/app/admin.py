from django.contrib import admin
from .models import Order, Nansu, OrderInfo, Calendar, Image, JanFront, JanBack, FebFront, FebBack, MarFront, MarBack, AprilFront, AprilBack, MayFront, MayBack, JuneFront, JuneBack, JulyFront, JulyBack, AugFront, AugBack, SepFront, SepBack, OctFront, OctBack, NovFront, NovBack, DecFront, DecBack, Prolog, Cover
from .forms import OrderForm
from django.db.models import F, Subquery, OuterRef
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
    actions = ['update_order_nansu']
    list_display = ('order_seq','user_name','user_phone','address','nansu','create_date','zipcode','postcode','detailAddress','order_date')
    def save_model(self, request, obj, form, change):
        if not change:  # 새로 생성되는 객체인 경우
            order_nansu = Order.objects.last()
            if order_nansu:
                obj.zipcode = order_nansu.zipcode + 1
            else:
                obj.zipcode = 1
        obj.save()
    form = OrderForm
    
    def update_order_nansu(self, request, queryset):
        # Nansu 테이블과 연결된 Order 테이블의 nansu 필드를 업데이트할 때 사용할 Subquery를 정의합니다.
        nansu_subquery = Nansu.objects.filter(nansu_seq=OuterRef('order_seq')).values('nansu')[:1]

        # Order 테이블의 nansu 필드를 Nansu 테이블의 nansu 필드 값으로 업데이트합니다.
        Order.objects.update(nansu=Subquery(nansu_subquery))

        self.message_user(request, f"{queryset.count()} 개의 난수가 수정 되었습니다.")
    update_order_nansu.short_description = "난수 입력(Nansu페이지의 nansu필드 데이터가 입력됩니다.)"



admin.site.register(Order, OrderAdmin)

# admin.site.register(Order, OrderAdmin)
class NansuAdmin(admin.ModelAdmin): #난수 생성 액션
    actions = ['insert_random_nansu']
    ordering = ['-nansu_seq']
    list_display = ('nansu_seq','nansu','nansu_state','permission','created_at')

    def insert_random_nansu(self, request, queryset):
        for obj in queryset:
            obj.nansu = str(random.randint(10**(8-1), (10**8)-1))
            obj.save()
        self.message_user(request, f"{queryset.count()} 개의 난수가 생성 되었습니다.")
    insert_random_nansu.short_description = "난수 생성"

    def update_date_field(self, request, queryset): #사용 안 함.
        updated_count = queryset.update(created_at=now().date())
        self.message_user(request, f"{queryset.count()} 개의 날짜 정보가 등록 되었습니다.")
    update_date_field.short_description="날짜 생성 액션(필수)"


    def save_model(self, request, obj, form, change):
        if not change:  # 새로 생성되는 객체인 경우
            last_nansu = Nansu.objects.last()
            if last_nansu:
                obj.nansu_seq = last_nansu.nansu_seq + 1
            else:
                obj.nansu_seq = 1
        obj.save()

admin.site.register(Nansu, NansuAdmin)

