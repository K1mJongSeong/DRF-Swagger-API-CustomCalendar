from django.contrib import admin
from django.urls import path
from app import views
from app.views import HelloWorld
from app.views import NansuList, NansuUrlDetail




urlpatterns = [
    path('admin/', admin.site.urls), #localhost:8000/admin/ 경로입니다. admin.site.urls 함수가 호출됩니다.
    path('nansu/', views.nansu, name='nansu'), 
    path('',views.index),#root url을 의미합니다. views.index 함수가 호출됩니다.
    path('hello/', HelloWorld.as_view()),
    path('NansuList',NansuList.as_view()),
    path('NansuUrlDetail/<int:nansu>/', NansuUrlDetail.as_view()),
]
