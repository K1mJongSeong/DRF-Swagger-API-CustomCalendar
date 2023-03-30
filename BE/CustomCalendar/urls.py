from django.contrib import admin
from django.urls import path ,include
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from rest_framework import routers
from rest_framework.decorators import api_view
from rest_framework_swagger.views import get_swagger_view
from app import views
from app.admin import NansuInfoAdmin
#from app.admin import NansuInfoDetail
from app.views import NansuList, NansuUrlDetail, CalendarUrlDetail, ImageView, SwaggerSchemaView, JanFrontPutView, JanBackPutView, FebFrontPutView, FebBackPutView, MarFrontPutView, MarBackPutView, AprilFrontPutView, AprilBackPutView, MayFrontPutView, MayBackPutView, JuneFrontPutView, JuneBackPutView, JulyFrontPutView, JulyBackPutView, AugFrontPutView, AugBackPutView, SepFrontPutView, SepBackPutView, OctFrontPutView, OctBackPutView, NovFrontPutView, NovBackPutView, DecFrontPutView, DecBackPutView, PrologPutView, CoverPutView
from app.views import OrderList, OrderInfoList, CalendarList, OrderUrlDetail, JanFront, JanBack, FebFront, FebBack, MarFront, MarBack, AprilFront, AprilBack, MayFront, MayBack, JuneFront, JuneBack, JulyFront, JulyBack, AugFront, AugBack, SepFront, SepBack, OctFront, OctBack, NovFront, NovBack, DecFront, DecBack, Prolog, Cover, CustomLogoutView, NoticePostView, NoticeListView, NoticePutView, NoticeDeleteView

schema_view = get_schema_view(
    openapi.Info(
        title="Open API", #타이틀
        default_version='v1', #버전
        description="시스템 API", #설명
        terms_of_service="https://www.google.com/policies/terms/",
    ),
    public=True,
    permission_classes=(AllowAny,),
) #Swagger API문서 스키마


urlpatterns = [
    path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),#Swagger API PATH
    path('admin/', admin.site.urls), #localhost:8000/admin/ 경로입니다. admin.site.urls 함수가 호출됩니다.
    path('custom_logout/', CustomLogoutView.as_view(), name='custom_logout'),
    path('nansu/', views.nansu, name='nansu'), 
    #path('',views.index),#root url을 의미합니다. views.index 함수가 호출됩니다. 
    path('NansuList/',NansuList.as_view()),
    path('OrderUrlDetail/<str:nansu>/', OrderUrlDetail.as_view(), name='OrderUrlDetail'), #url에 OrderList/1/ 식으로 접속하면 seq 1번으로 저장된 JSON 데이터 받아옴.
    path('OrderList/',OrderList.as_view()),
    #path('OrderInfoList/', OrderInfoList.as_view()),
    #path('CalendarList/', CalendarList.as_view()),
    path('NansuUrlDetail/<str:nansu>/', NansuUrlDetail.as_view()),
    #path('CalendarUrlDetail/<int:calendar>/',CalendarUrlDetail.as_view()),
    path('JanFront/',JanFront.as_view()),
    path('JanFrontPut/<str:nansu>/',JanFrontPutView.as_view()),
    path('JanBackPut/<str:nansu>/',JanBackPutView.as_view()),
    path('FebFrontPut/<str:nansu>/',FebFrontPutView.as_view()),
    path('FebBackPut/<str:nansu>/',FebBackPutView.as_view()),
    path('MarFrontPut/<str:nansu>/',MarFrontPutView.as_view()),
    path('MarBackPut/<str:nansu>/',MarBackPutView.as_view()),
    path('AprilFrontPut/<str:nansu>/',AprilFrontPutView.as_view()),
    path('AprilBackPut/<str:nansu>/',AprilBackPutView.as_view()),
    path('MayFrontPut/<str:nansu>/',MayFrontPutView.as_view()),
    path('MayBackPut/<str:nansu>/',MayBackPutView.as_view()),
    path('JuneFrontPut/<str:nansu>/',JuneFrontPutView.as_view()),
    path('JuneBackPut/<str:nansu>/',JuneBackPutView.as_view()),
    path('JulyFrontPut/<str:nansu>/',JulyFrontPutView.as_view()),
    path('JulyBackPut/<str:nansu>/',JulyBackPutView.as_view()),
    path('AugFrontPut/<str:nansu>/',AugFrontPutView.as_view()),
    path('AugBackPut/<str:nansu>/',AugBackPutView.as_view()),
    path('SepFrontPut/<str:nansu>/',SepFrontPutView.as_view()),
    path('SepBackPut/<str:nansu>/',SepBackPutView.as_view()),
    path('OctFrontPut/<str:nansu>/',OctFrontPutView.as_view()),
    path('OctBackPut/<str:nansu>/',OctBackPutView.as_view()),
    path('NovFrontPut/<str:nansu>/',NovFrontPutView.as_view()),
    path('NovBackPut/<str:nansu>/',NovBackPutView.as_view()),
    path('DecFrontPut/<str:nansu>/',DecFrontPutView.as_view()),
    path('DecBackPut/<str:nansu>/',DecBackPutView.as_view()),
    path('PrologPut/<str:nansu>/',PrologPutView.as_view()),
    path('CoverPut/<str:nansu>/',CoverPutView.as_view()),
    path('JanBack/',JanBack.as_view()),
    #path('JanBackPut/<str:nansu>/',JanBackPutView.as_view()),
    path('FebFront/',FebFront.as_view()),
    path('FebBack/',FebBack.as_view()),
    path('MarFront/',MarFront.as_view()),
    path('MarBack/',MarBack.as_view()),
    path('AprilFront/',AprilFront.as_view()),
    path('AprilBack/',AprilBack.as_view()),
    path('MayFront/',MayFront.as_view()),
    path('MayBack/',MayBack.as_view()),
    path('JuneFront/',JuneFront.as_view()),
    path('JuneBack/',JuneBack.as_view()),
    path('JulyFront/',JulyFront.as_view()),
    path('JulyBack/',JulyBack.as_view()),
    path('AugFront/',AugFront.as_view()),
    path('AugBack/',AugBack.as_view()),
    path('SepFront/',SepFront.as_view()),
    path('SepBack/',SepBack.as_view()),
    path('OctFront/',OctFront.as_view()),
    path('OctBack/',OctBack.as_view()),
    path('NovFront/',NovFront.as_view()),
    path('NovBack/',NovBack.as_view()),
    path('DecFront/',DecFront.as_view()),
    path('DecBack/',DecBack.as_view()),
    path('Prolog/',Prolog.as_view()),
    path('Cover/',Cover.as_view()),
    path('Image/',ImageView.as_view()),
    #path('NoticeDetail/<str:nansu>/',NoticeView.as_view()),
    path('NoticePost/',NoticePostView.as_view()),
    path('NoticeList/',NoticeListView.as_view()),
    path('NoticePut/<str:nansu>/',NoticePutView.as_view()),
    path('NoticeDelete/<str:nansu>/',NoticeDeleteView.as_view()),
    #path('MonthGET/<int:page_num>/',MonthAPI2.as_view()),
    #path('NoticePost/',NoticePost.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#_media에 이미지 저장.


