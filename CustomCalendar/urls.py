from django.contrib import admin
from django.urls import path
from app import views



urlpatterns = [
    path('admin/', admin.site.urls), #localhost:8000/admin/ 경로입니다. admin.site.urls 함수가 호출됩니다.
    path('', views.index), #root url을 의미합니다. views.index 함수가 호출됩니다.
]
