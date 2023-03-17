from django.contrib import admin
from .models import Order, Nansu, OrderInfo, Calendar, Image, JanFront, JanBack, FebFront, FebBack, MarFront, MarBack, AprilFront, AprilBack, MayFront, MayBack, JuneFront, JuneBack, JulyFront, JulyBack, AugFront, AugBack, SepFront, SepBack, OctFront, OctBack, NovFront, NovBack, DecFront, DecBack, Prolog, Cover, Notice
from .forms import OrderForm
from django.db.models import F, Subquery, OuterRef
from django.utils.timezone import now
import random

admin.site.register(Calendar)
admin.site.register(Image)
admin.site.register(Prolog)
admin.site.register(Cover)

class JanFrontAdmin(admin.ModelAdmin):
    #actions = ['update_order_nansu','update_notice_memo']
    list_display = ('jan_nansu','jan_memo','jan_pic','jan_seq')
    # def update_order_nansu(self, request, queryset):
    #     # Nansu 테이블과 연결된 JanFront 테이블의 jan_nansu 필드를 업데이트할 때 사용할 Subquery를 정의합니다.
    #     nansu_subquery = Nansu.objects.filter(nansu_seq=OuterRef('jan_seq')).values('nansu')[:1]

    #     # JanFront 테이블의 jan_nansu 필드를 Nansu 테이블의 nansu 필드 값으로 업데이트합니다.
    #     JanFront.objects.update(jan_nansu=Subquery(nansu_subquery))

    #     self.message_user(request, f"{queryset.count()} 개의 난수가 수정 되었습니다.")
    # update_order_nansu.short_description = "난수 입력(Nansu페이지의 nansu필드 데이터가 입력됩니다.)"

    # def update_notice_memo(self, request, queryset):
    #     # JanFront 테이블과 연결된 Notice 테이블의 jan_memo 필드를 업데이트할 때 사용할 Subquery를 정의합니다.
    #     notice_subquery = Notice.objects.filter(notice_idx=OuterRef('jan_idx')).values('notice')[:1]

    #     # JanFront 테이블의 jan_memo 필드를 Notice 테이블의 notice 필드 값으로 업데이트합니다.
    #     JanFront.objects.update(jan_memo=Subquery(notice_subquery))

    #     self.message_user(request, f"{queryset.count()} 개의 난수가 수정 되었습니다.")
    # update_notice_memo.short_description = "메모 필드를 가져옵니다."

admin.site.register(JanFront, JanFrontAdmin)

class JanBackAdmin(admin.ModelAdmin):
    list_display = ('jan_nansu','jan_memo','jan_pic','jan_seq')
admin.site.register(JanBack, JanBackAdmin)

class FebFrontAdmin(admin.ModelAdmin):
    list_display = ('feb_nansu','feb_memo','feb_pic','feb_seq')
admin.site.register(FebFront, FebFrontAdmin)

class FebBackAdmin(admin.ModelAdmin):
    list_display = ('feb_nansu','feb_memo','feb_pic','feb_seq')
admin.site.register(FebBack, FebBackAdmin)


class MarFrontAdmin(admin.ModelAdmin):
    list_display = ('mar_nansu','mar_memo','mar_pic','mar_seq')
admin.site.register(MarFront, MarFrontAdmin)

class MarBackAdmin(admin.ModelAdmin):
    list_display = ('mar_nansu','mar_memo','mar_pic','mar_seq')
admin.site.register(MarBack, MarBackAdmin)


class AprilFrontAdmin(admin.ModelAdmin):
    list_display = ('april_nansu','april_memo','april_pic','april_seq')
admin.site.register(AprilFront, AprilFrontAdmin)

class AprilBackAdmin(admin.ModelAdmin):
    list_display = ('april_nansu','april_memo','april_pic','april_seq')
admin.site.register(AprilBack, AprilBackAdmin)


class MayFrontAdmin(admin.ModelAdmin):
    list_display = ('may_nansu','may_memo','may_pic','may_seq')
admin.site.register(MayFront, MayFrontAdmin)

class MayBackAdmin(admin.ModelAdmin):
    list_display = ('may_nansu','may_memo','may_pic','may_seq')
admin.site.register(MayBack, MayBackAdmin)


class JuneFrontAdmin(admin.ModelAdmin):
    list_display = ('june_nansu','june_memo','june_pic','june_seq')
admin.site.register(JuneFront, JuneFrontAdmin)

class JuneBackAdmin(admin.ModelAdmin):
    list_display = ('june_nansu','june_memo','june_pic','june_seq')
admin.site.register(JuneBack, JuneBackAdmin)


class JulyFrontAdmin(admin.ModelAdmin):
    list_display = ('july_nansu','july_memo','july_pic','july_seq')
admin.site.register(JulyFront, JulyFrontAdmin)

class JulyBackAdmin(admin.ModelAdmin):
    list_display = ('july_nansu','july_memo','july_pic','july_seq')
admin.site.register(JulyBack, JulyBackAdmin)


class AugFrontAdmin(admin.ModelAdmin):
    list_display = ('aug_nansu','aug_memo','aug_pic','aug_seq')
admin.site.register(AugFront, AugFrontAdmin)

class AugBackAdmin(admin.ModelAdmin):
    list_display = ('aug_nansu','aug_memo','aug_pic','aug_seq')
admin.site.register(AugBack, AugBackAdmin)


class SepFrontAdmin(admin.ModelAdmin):
    list_display = ('sep_nansu','sep_memo','sep_pic','sep_seq')
admin.site.register(SepFront, SepFrontAdmin)

class SepBackAdmin(admin.ModelAdmin):
    list_display = ('sep_nansu','sep_memo','sep_pic','sep_seq')
admin.site.register(SepBack, SepBackAdmin)


class OctFrontAdmin(admin.ModelAdmin):
    list_display = ('oct_nansu','oct_memo','oct_pic','oct_seq')
admin.site.register(OctFront, OctFrontAdmin)

class OctBackAdmin(admin.ModelAdmin):
    list_display = ('oct_nansu','oct_memo','oct_pic','oct_seq')
admin.site.register(OctBack, OctBackAdmin)


class DecFrontAdmin(admin.ModelAdmin):
    list_display = ('dec_nansu','dec_memo','dec_pic','dec_seq')
admin.site.register(DecFront, DecFrontAdmin)

class DecBackAdmin(admin.ModelAdmin):
    list_display = ('dec_nansu','dec_memo','dec_pic','dec_seq')
admin.site.register(DecBack, DecBackAdmin)

class NoticeAdmin(admin.ModelAdmin):
    list_display =('nansu','monthdays','notice','notice_idx')
    # actions = ['update_notice_nansu']
    # def update_notice_nansu(self, request, queryset):
    #     # Nansu 테이블과 연결된 Notice 테이블의 nansu 필드를 업데이트할 때 사용할 Subquery를 정의합니다.
    #     nansu_subquery = Nansu.objects.filter(nansu_seq=OuterRef('notice_idx')).values('nansu')[:1]

    #     # Order 테이블의 nansu 필드를 Nansu 테이블의 nansu 필드 값으로 업데이트합니다.
    #     Notice.objects.update(nansu=Subquery(nansu_subquery))

    #     self.message_user(request, f"{queryset.count()} 개의 난수가 수정 되었습니다.")
    # update_notice_nansu.short_description = "난수 입력(Nansu페이지의 nansu필드 데이터가 입력됩니다.)"

admin.site.register(Notice, NoticeAdmin)

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

