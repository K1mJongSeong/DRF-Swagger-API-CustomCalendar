from django.contrib import admin
from django.urls import path ,include
from app import views
from app.views import NansuList, NansuUrlDetail
from app.views import OrderList, OrderInfoList, CalendarList




urlpatterns = [
    path('admin/', admin.site.urls), #localhost:8000/admin/ 경로입니다. admin.site.urls 함수가 호출됩니다.
    path('nansu/', views.nansu, name='nansu'), 
    path('',views.index),#root url을 의미합니다. views.index 함수가 호출됩니다. 
    path('NansuList/',NansuList.as_view()),
    path('OrderList/<int:pk>/', OrderList.as_view(), name='OrderList'), #url에 OrderList/1/ 식으로 접속하면 seq 1번으로 저장된 JSON 데이터 받아옴.
    path('OrderInfoList/', OrderInfoList.as_view()),
    path('CalendarList/', CalendarList.as_view()),
    path('NansuUrlDetail/<int:nansu>/', NansuUrlDetail.as_view()),
]
