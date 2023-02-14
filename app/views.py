from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("TEST PAGE")

# Create your views here.
