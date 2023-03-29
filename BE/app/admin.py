from django.contrib import admin
from django.apps import AppConfig
from django.conf import settings
from .models import Order, Nansu, OrderInfo, Calendar, Image, JanFront, JanBack, FebFront, FebBack, MarFront, MarBack, AprilFront, AprilBack, MayFront, MayBack, JuneFront, JuneBack, JulyFront, JulyBack, AugFront, AugBack, SepFront, SepBack, OctFront, OctBack, NovFront, NovBack, DecFront, DecBack, Prolog, Cover, Notice, NansuInfo, NansuSession
from .forms import OrderForm, NoticeForm
from django.urls import path
from django.db.models import F, Subquery, OuterRef
from django.utils.timezone import now
from django.utils import timezone
from datetime import timedelta
from django.http import HttpResponseRedirect
from django.utils.html import format_html
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db import connection, models
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime
from django.contrib.admin import AdminSite
import random
import string

admin.site.site_header = '모바일 달력커스텀 인쇄주문'
admin.site.index_title = '모바일 달력커스텀 인쇄주문'
# admin.site.register(Calendar)
# admin.site.register(Prolog)
# admin.site.register(Cover)

class YourAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self):
        if settings.ADMIN_LOGOUT_PRESERVE_SESSION:
            import app.signals

# class JanFrontAdmin(admin.ModelAdmin):
#     #actions = ['update_order_nansu','update_notice_memo']
#     list_display = ('nansu','pic','jan_seq')
#     # def update_order_nansu(self, request, queryset):
#     #     # Nansu 테이블과 연결된 JanFront 테이블의 jan_nansu 필드를 업데이트할 때 사용할 Subquery를 정의합니다.
#     #     nansu_subquery = Nansu.objects.filter(nansu_seq=OuterRef('jan_seq')).values('nansu')[:1]

#     #     # JanFront 테이블의 jan_nansu 필드를 Nansu 테이블의 nansu 필드 값으로 업데이트합니다.
#     #     JanFront.objects.update(jan_nansu=Subquery(nansu_subquery))

#     #     self.message_user(request, f"{queryset.count()} 개의 난수가 수정 되었습니다.")
#     # update_order_nansu.short_description = "난수 입력(Nansu페이지의 nansu필드 데이터가 입력됩니다.)"

#     # def update_notice_memo(self, request, queryset):
#     #     # JanFront 테이블과 연결된 Notice 테이블의 jan_memo 필드를 업데이트할 때 사용할 Subquery를 정의합니다.
#     #     notice_subquery = Notice.objects.filter(notice_idx=OuterRef('jan_idx')).values('notice')[:1]

#     #     # JanFront 테이블의 jan_memo 필드를 Notice 테이블의 notice 필드 값으로 업데이트합니다.
#     #     JanFront.objects.update(jan_memo=Subquery(notice_subquery))

#     #     self.message_user(request, f"{queryset.count()} 개의 난수가 수정 되었습니다.")
#     # update_notice_memo.short_description = "메모 필드를 가져옵니다."

# admin.site.register(JanFront, JanFrontAdmin)

# class JanBackAdmin(admin.ModelAdmin):
#     list_display = ('nansu','pic','jan_seq')
# admin.site.register(JanBack, JanBackAdmin)

# class FebFrontAdmin(admin.ModelAdmin):
#     list_display = ('nansu','pic','feb_seq')
# admin.site.register(FebFront, FebFrontAdmin)

# class FebBackAdmin(admin.ModelAdmin):
#     list_display = ('nansu','pic','feb_seq')
# admin.site.register(FebBack, FebBackAdmin)


# class MarFrontAdmin(admin.ModelAdmin):
#     list_display = ('nansu','pic','mar_seq')
# admin.site.register(MarFront, MarFrontAdmin)

# class MarBackAdmin(admin.ModelAdmin):
#     list_display = ('nansu','pic','mar_seq')
# admin.site.register(MarBack, MarBackAdmin)


# class AprilFrontAdmin(admin.ModelAdmin):
#     list_display = ('nansu','pic','april_seq')
# admin.site.register(AprilFront, AprilFrontAdmin)

# class AprilBackAdmin(admin.ModelAdmin):
#     list_display = ('nansu','pic','april_seq')
# admin.site.register(AprilBack, AprilBackAdmin)


# class MayFrontAdmin(admin.ModelAdmin):
#     list_display = ('nansu','pic','may_seq')
# admin.site.register(MayFront, MayFrontAdmin)

# class MayBackAdmin(admin.ModelAdmin):
#     list_display = ('nansu','pic','may_seq')
# admin.site.register(MayBack, MayBackAdmin)


# class JuneFrontAdmin(admin.ModelAdmin):
#     list_display = ('nansu','pic','june_seq')
# admin.site.register(JuneFront, JuneFrontAdmin)

# class JuneBackAdmin(admin.ModelAdmin):
#     list_display = ('nansu','pic','june_seq')
# admin.site.register(JuneBack, JuneBackAdmin)


# class JulyFrontAdmin(admin.ModelAdmin):
#     list_display = ('nansu','pic','july_seq')
# admin.site.register(JulyFront, JulyFrontAdmin)

# class JulyBackAdmin(admin.ModelAdmin):
#     list_display = ('nansu','pic','july_seq')
# admin.site.register(JulyBack, JulyBackAdmin)


# class AugFrontAdmin(admin.ModelAdmin):
#     list_display = ('nansu','pic','aug_seq')
# admin.site.register(AugFront, AugFrontAdmin)

# class AugBackAdmin(admin.ModelAdmin):
#     list_display = ('nansu','pic','aug_seq')
# admin.site.register(AugBack, AugBackAdmin)


# class SepFrontAdmin(admin.ModelAdmin):
#     list_display = ('nansu','pic','sep_seq')
# admin.site.register(SepFront, SepFrontAdmin)

# class SepBackAdmin(admin.ModelAdmin):
#     list_display = ('nansu','pic','sep_seq')
# admin.site.register(SepBack, SepBackAdmin)


# class OctFrontAdmin(admin.ModelAdmin):
#     list_display = ('nansu','pic','oct_seq')
# admin.site.register(OctFront, OctFrontAdmin)

# class OctBackAdmin(admin.ModelAdmin):
#     list_display = ('nansu','pic','oct_seq')
# admin.site.register(OctBack, OctBackAdmin)


# class DecFrontAdmin(admin.ModelAdmin):
#     list_display = ('nansu','pic','dec_seq')
# admin.site.register(DecFront, DecFrontAdmin)

# class DecBackAdmin(admin.ModelAdmin):
#     list_display = ('nansu','pic','dec_seq')
# admin.site.register(DecBack, DecBackAdmin)

# class NoticeAdmin(admin.ModelAdmin):
#     list_display =('nansu','monthdays','notice')
#     form = NoticeForm
#     # actions = ['update_notice_nansu']
#     # def update_notice_nansu(self, request, queryset):
#     #     # Nansu 테이블과 연결된 Notice 테이블의 nansu 필드를 업데이트할 때 사용할 Subquery를 정의합니다.
#     #     nansu_subquery = Nansu.objects.filter(nansu_seq=OuterRef('notice_idx')).values('nansu')[:1]

#     #     # Order 테이블의 nansu 필드를 Nansu 테이블의 nansu 필드 값으로 업데이트합니다.
#     #     Notice.objects.update(nansu=Subquery(nansu_subquery))

#     #     self.message_user(request, f"{queryset.count()} 개의 난수가 수정 되었습니다.")
#     # update_notice_nansu.short_description = "난수 입력(Nansu페이지의 nansu필드 데이터가 입력됩니다.)"

# admin.site.register(Notice, NoticeAdmin)

class OrderAdmin(admin.ModelAdmin):
    actions = ['update_order_nansu']
    search_fields = ['nansu']
    ordering = ['-order_date','-create_date']
    list_filter = ['orderState']
    list_display = ('order_seq','nansu','orderState','user_name','user_phone','address','postcode','detailAddress','order_date','create_date')
    list_per_page = 20
    

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


class NansuAdmin(admin.ModelAdmin): #난수 생성 액션
    actions = ['insert_random_nansu']
    search_fields = ['nansu','nansu_type']
    ordering = ['-nansu_seq']
    list_display = ('nansu_seq','nansu','nansu_type','created_at')
    change_form_template = "admin/button.html"
    list_per_page = 20
    fields = ['nansu_type']
    print(change_form_template)

    def nansu_view(self, request, object_id=None, extra_context=None):
        print('nansu_view 실행')
        if "_insert-random" in request.POST:
            nansu_option = request.POST.get('nansu')
            nansu_type = request.POST.get('nansu_type')
            create_date = request.POST.get('create_at')
            info_seq = request.POST.get('info_seq')
            print('11111')
            print(create_date)
            nansu_list = []
            session_dict = request.session.get('session_dict', {})  # 기존 세션 딕셔너리 가져오기
            for _ in range(int(nansu_option)):
                random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
                new_nansu = Nansu(nansu=random_string, nansu_type=nansu_type,nansu_state='정상')
                new_nansu.save()
                nansu_list.append(new_nansu)
            
            new_nansu_info = NansuInfo(nansu_count=int(nansu_option), nansu_date=datetime.now(), template_name=nansu_type, session_data=session_dict)
            new_nansu_info.save()
            print(nansu_list)
            print(random_string)

            new_nansu_session = NansuSession(session_nansu=random_string, session_nansu_type=nansu_type, expire_date=timezone.now(), session_nansu_option=nansu_option,session_nansu_seq=info_seq)# + datetime.timedelta(days=1))
            new_nansu_session.save()
            request.session['nansu_session_id'] = new_nansu_session.pk
            print(new_nansu_session.pk)

            # 세션에 nansu_seq 값 저장
            nansu_seq_list = [nansu.nansu_seq for nansu in nansu_list]
            request.session['nansu_seq'] =  nansu_option#new_nansu.nansu_seq
            request.session['nansu'] = nansu_seq_list
            request.session['nansu_type'] = nansu_type
            print(nansu_option)
            print(nansu_seq_list)

            

            # 새로운 info_seq에 대한 세션 정보 추가
            if new_nansu_info:
                nansu_seq_list = [nansu.nansu_seq for nansu in nansu_list]
                session_dict[new_nansu_info.info_seq] = {
                    'nansu_seq': nansu_option,
                    'nansu': nansu_seq_list,
                    'nansu_type': nansu_type,
                }
                request.session['session_dict'] = session_dict  # 세션 딕셔너리 업데이트
            print(session_dict)

            self.message_user(request, f"{nansu_option} 개의 난수가 생성 되었습니다.")
            request.session.modified = True
            return HttpResponseRedirect(request.path)

        nansu_seq = request.session.get('nansu_seq', None) # 저장된 nansu_seq 값을 가져오기
        session_dict = request.session.get('session_dict', {})

        # 새로운 info_seq에 대한 세션 정보가 있다면 해당 정보로 업데이트
        if object_id in session_dict:
            request.session['nansu_seq'] = session_dict[object_id]['nansu_seq']
            request.session['nansu'] = session_dict[object_id]['nansu']
            request.session['nansu_type'] = session_dict[object_id]['nansu_type']
            nansu_list = Nansu.objects.filter(nansu_seq__in=session_dict[object_id]['nansu']).order_by('-created_at')
        else:
            # 세션에서 nansu_option에 해당하는 정보가 없으면 기존 로직대로 처리
            if nansu_seq == "1":
                nansu_list = Nansu.objects.filter

        return super().changeform_view(request, object_id, extra_context=extra_context)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        print('changeform_view 실행')
        extra_context = extra_context or {}
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = False
        return self.nansu_view(request, object_id=object_id, extra_context=extra_context)


    def insert_random_nansu(self, request, queryset):
        print('c')
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



class NansuInfoAdmin(admin.ModelAdmin):
    list_display = ('info_seq', 'template_name', 'nansu_date', 'nansu_count')
    list_per_page = 20

    def change_view(self, request, object_id, form_url='', extra_context=None):
        nansu_info = NansuInfo.objects.get(pk=object_id)
        session_data = nansu_info.session_data
        print('asd123')
        print(session_data)
        if session_data:
            session_dict = session_data
        else:
            session_dict = request.session.get('session_dict',{})
        #session_dict = request.session.get('session_dict', {})
        nansu_list = []
        # 세션 정보 가져오기
        session_id = request.session.get('nansu_session_id', None)
        print(session_id)
        # if session_id:
        #     try:
        #         nansu_session = NansuSession.objects.get(pk=session_id)
        #         nansu_list = nansu_session.session_nansu.split(',')
        #         nansu_type = nansu_session.session_nansu_type
        #         nansu_option = nansu_session.session_nansu_option # add this line
        #         nansu_seq = nansu_session.session_nansu_seq # add this line
        #         nansu_objects = Nansu.objects.filter(nansu_seq__in=nansu_list).order_by('-created_at')
        #     except NansuSession.DoesNotExist:
        #         pass
        # nansu_option = None
        
        if object_id in session_dict:
            nansu_list = session_dict[object_id]['nansu']
            nansu_type = session_dict[object_id]['nansu_type']
            nansu_option = session_dict[object_id]['nansu_seq']
            nansu_objects = Nansu.objects.filter(nansu_seq__in=nansu_list).order_by('-created_at')
        else:
            nansu_type = nansu_info.template_name
            nansu_objects = Nansu.objects.filter(nansu_type=nansu_type).order_by('-created_at')
        print(session_dict)
        print('bbb123123')
        context = {
            'nansu_info': nansu_info,
            'nansu_list': nansu_objects,
            'nansu_type': nansu_type,
            # 'nansu_option': nansu_option, # pass nansu_option to context
            # 'nansu_seq': nansu_seq, # pass nansu_seq to context
        }

        return render(request, 'admin/nansu_info.html', context)

admin.site.register(NansuInfo, NansuInfoAdmin)

# class NansuInfoAdmin(admin.ModelAdmin):
#     list_display = ('info_seq', 'template_name', 'nansu_date', 'nansu_count')
#     list_per_page = 20

#     def change_view(self, request, object_id, form_url='', extra_context=None):
#         nansu_info = NansuInfo.objects.get(pk=object_id)
#         session_dict = request.session.get('session_dict', {})
#         nansu_list = []
#         # 세션 정보 가져오기
#         session_id = request.session.get('nansu_session_id', None)
#         print(session_id)
#         if session_id:
#             try:
#                 nansu_session = NansuSession.objects.get(pk=session_id)
#                 nansu_list = nansu_session.session_nansu.split(',')
#                 nansu_type = nansu_session.session_nansu_type
#                 nansu_option = nansu_session.session_nansu
#                 nansu_objects = Nansu.objects.filter(nansu_seq__in=nansu_list).order_by('-created_at')
#             except NansuSession.DoesNotExist:
#                 pass
#         #nansu_option = None
#         print(session_dict)
#         if object_id in session_dict:
#             nansu_list = session_dict[object_id]['nansu']
#             nansu_type = session_dict[object_id]['nansu_type']
#             nansu_option = session_dict[object_id]['nansu_seq']
#             nansu_objects = Nansu.objects.filter(nansu_seq__in=nansu_list).order_by('-created_at')
#         else:
#             nansu_type = nansu_info.template_name
#             nansu_objects = Nansu.objects.filter(nansu_type=nansu_type).order_by('-created_at')

#         context = {
#             'nansu_info': nansu_info,
#             'nansu_list': nansu_objects,
#             'nansu_type': nansu_type,
#             'nansu_option': nansu_option,
#         }

#         return render(request, 'admin/nansu_info.html', context)

# admin.site.register(NansuInfo, NansuInfoAdmin)



# class NansuInfoAdmin(admin.ModelAdmin):
#     list_display = ('info_seq', 'template_name', 'nansu_date', 'nansu_count')

#     def change_view(self, request, object_id, form_url='', extra_context=None):
#         nansu_info = NansuInfo.objects.get(pk=object_id)
#         nansu_list = request.session.get('nansu', []) # 수정된 부분
#         nansu_type = request.session.get('nansu_type', None)
#         nansu_option = request.session.get('nansu_seq', None)
#         print(nansu_list)
#         print(nansu_option)

#         if nansu_option == "1":
#             nansu_list = Nansu.objects.filter(nansu_seq__in=nansu_list).order_by('-created_at')
#             print('성공1')
#         elif nansu_option == "10":
#             nansu_list = Nansu.objects.filter(nansu_seq__in=nansu_list).order_by('-created_at')
#             print('성공10')
#         elif nansu_option == "100":
#             nansu_list = Nansu.objects.filter(nansu_seq__in=nansu_list).order_by('-created_at')
#             print('성공100')
#         else:
#             nansu_list = Nansu.objects.filter(nansu_type=nansu_info.template_name).order_by('-created_at')
#             print('실패')
#         print(nansu_list.count())
#         print(nansu_type)

#         context = {
#             'nansu_info':nansu_info,
#             'nansu_list':nansu_list,
#         }

#         return render(request,'admin/nansu_info.html',context)
# admin.site.register(NansuInfo, NansuInfoAdmin)
