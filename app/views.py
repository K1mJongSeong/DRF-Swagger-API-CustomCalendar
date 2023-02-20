from django.shortcuts import render
from django.http import HttpResponse
from .models import Nansu

def index(request):
    return HttpResponse("TEST PAGE")

def nansu(request):
    nansuTest = Nansu.objects.filter(nansu_state='정상')
    print(nansuTest)
    return render(request,'index.html', {"nansuTest":nansuTest})

