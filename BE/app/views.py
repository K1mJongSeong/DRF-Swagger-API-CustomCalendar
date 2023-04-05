from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout
from django.db import models
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import ListView, DetailView
from rest_framework_swagger.renderers import SwaggerUIRenderer
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import api_view, renderer_classes, parser_classes #api
from rest_framework import status, generics, viewsets, serializers
from rest_framework.parsers import FileUploadParser,MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema, force_serializer_instance
from drf_yasg import openapi
from .models import Nansu, Order, OrderInfo, Calendar, JanFront, JanBack, FebFront, FebBack, MarFront, MarBack, AprilFront, AprilBack, MayFront, MayBack, JuneFront, JuneBack, JulyFront, JulyBack, AugFront, AugBack, SepFront, SepBack, OctFront, OctBack, NovFront, NovBack, DecFront, DecBack, Prolog, Cover, Image, Notice, NansuInfo
from .serializers import NansuSerializer, OrderSerializer, OrderInfoSerializer, CalendarSerializer, JanFrontSerializer, JanBackSerializer, FebFrontSerializer, FebBackSerializer, MarFrontSerializer, MarBackSerializer,AprilFrontSerializer,AprilBackSerializer,MayFrontSerializer,MayBackSerializer, JuneFrontSerializer, JuneBackSerializer, JulyFrontSerializer, JulyBackSerializer, AugFrontSerializer, AugBackSerializer, SepFrontSerializer, SepBackSerializer, OctFrontSerializer, OctBackSerializer, NovFrontSerializer, NovBackSerializer, DecFrontSerializer, DecBackSerializer, PrologSerializer, CoverSerializer, ImageSerializer, NoticeSerializer, NansuInfoSerializer
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth import logout
from django.contrib.auth.models import AnonymousUser
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
import csv


class JanFrontPutView(generics.UpdateAPIView):
    serializer_class = JanFrontSerializer
    queryset = JanFront.objects.all()
    lookup_field = 'nansu'

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.filter(nansu=self.kwargs[self.lookup_field]).first()
        if not obj:
            raise Http404(f"No {self.lookup_field} matching the query")
        return obj

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        nansu = request.data.get('nansu')
        if nansu and nansu != instance.nansu:
            raise serializers.ValidationError("Invalid value for 'nansu'")
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(pic=serializer.validated_data['pic'])


class JanBackPutView(generics.UpdateAPIView):
    serializer_class = JanBackSerializer
    queryset = JanBack.objects.all()
    lookup_field = 'nansu'

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.filter(nansu=self.kwargs[self.lookup_field]).first()
        if not obj:
            raise Http404(f"No {self.lookup_field} matching the query")
        return obj

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        nansu = request.data.get('nansu')
        if nansu and nansu != instance.nansu:
            raise serializers.ValidationError("Invalid value for 'nansu'")
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(pic=serializer.validated_data['pic'])


class FebFrontPutView(generics.UpdateAPIView):
    serializer_class = FebFrontSerializer
    queryset = FebFront.objects.all()
    lookup_field = 'nansu'

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.filter(nansu=self.kwargs[self.lookup_field]).first()
        if not obj:
            raise Http404(f"No {self.lookup_field} matching the query")
        return obj

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        nansu = request.data.get('nansu')
        if nansu and nansu != instance.nansu:
            raise serializers.ValidationError("Invalid value for 'nansu'")
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(pic=serializer.validated_data['pic'])


class FebBackPutView(generics.UpdateAPIView):
    serializer_class = FebBackSerializer
    queryset = FebBack.objects.all()
    lookup_field = 'nansu'

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.filter(nansu=self.kwargs[self.lookup_field]).first()
        if not obj:
            raise Http404(f"No {self.lookup_field} matching the query")
        return obj

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        nansu = request.data.get('nansu')
        if nansu and nansu != instance.nansu:
            raise serializers.ValidationError("Invalid value for 'nansu'")
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(pic=serializer.validated_data['pic'])



class MarFrontPutView(generics.UpdateAPIView):
    serializer_class = MarFrontSerializer
    queryset = MarFront.objects.all()
    lookup_field = 'nansu'

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.filter(nansu=self.kwargs[self.lookup_field]).first()
        if not obj:
            raise Http404(f"No {self.lookup_field} matching the query")
        return obj

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        nansu = request.data.get('nansu')
        if nansu and nansu != instance.nansu:
            raise serializers.ValidationError("Invalid value for 'nansu'")
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(pic=serializer.validated_data['pic'])



class MarBackPutView(generics.UpdateAPIView):
    serializer_class = MarBackSerializer
    queryset = MarBack.objects.all()
    lookup_field = 'nansu'

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.filter(nansu=self.kwargs[self.lookup_field]).first()
        if not obj:
            raise Http404(f"No {self.lookup_field} matching the query")
        return obj

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        nansu = request.data.get('nansu')
        if nansu and nansu != instance.nansu:
            raise serializers.ValidationError("Invalid value for 'nansu'")
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(pic=serializer.validated_data['pic'])



class AprilFrontPutView(generics.UpdateAPIView):
    serializer_class = AprilFrontSerializer
    queryset = AprilFront.objects.all()
    lookup_field = 'nansu'

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.filter(nansu=self.kwargs[self.lookup_field]).first()
        if not obj:
            raise Http404(f"No {self.lookup_field} matching the query")
        return obj

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        nansu = request.data.get('nansu')
        if nansu and nansu != instance.nansu:
            raise serializers.ValidationError("Invalid value for 'nansu'")
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(pic=serializer.validated_data['pic'])


class AprilBackPutView(generics.UpdateAPIView):
    serializer_class = AprilBackSerializer
    queryset = AprilBack.objects.all()
    lookup_field = 'nansu'

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.filter(nansu=self.kwargs[self.lookup_field]).first()
        if not obj:
            raise Http404(f"No {self.lookup_field} matching the query")
        return obj

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        nansu = request.data.get('nansu')
        if nansu and nansu != instance.nansu:
            raise serializers.ValidationError("Invalid value for 'nansu'")
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(pic=serializer.validated_data['pic'])


class MayFrontPutView(generics.UpdateAPIView):
    serializer_class = MayFrontSerializer
    queryset = MayFront.objects.all()
    lookup_field = 'nansu'

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.filter(nansu=self.kwargs[self.lookup_field]).first()
        if not obj:
            raise Http404(f"No {self.lookup_field} matching the query")
        return obj

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        nansu = request.data.get('nansu')
        if nansu and nansu != instance.nansu:
            raise serializers.ValidationError("Invalid value for 'nansu'")
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(pic=serializer.validated_data['pic'])


class MayBackPutView(generics.UpdateAPIView):
    serializer_class = MayBackSerializer
    queryset = MayBack.objects.all()
    lookup_field = 'nansu'

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.filter(nansu=self.kwargs[self.lookup_field]).first()
        if not obj:
            raise Http404(f"No {self.lookup_field} matching the query")
        return obj

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        nansu = request.data.get('nansu')
        if nansu and nansu != instance.nansu:
            raise serializers.ValidationError("Invalid value for 'nansu'")
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(pic=serializer.validated_data['pic'])



class JuneFrontPutView(generics.UpdateAPIView):
    serializer_class = JuneFrontSerializer
    queryset = JuneFront.objects.all()
    lookup_field = 'nansu'

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.filter(nansu=self.kwargs[self.lookup_field]).first()
        if not obj:
            raise Http404(f"No {self.lookup_field} matching the query")
        return obj

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        nansu = request.data.get('nansu')
        if nansu and nansu != instance.nansu:
            raise serializers.ValidationError("Invalid value for 'nansu'")
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(pic=serializer.validated_data['pic'])


class JuneBackPutView(generics.UpdateAPIView):
    serializer_class = JuneBackSerializer
    queryset = JuneBack.objects.all()
    lookup_field = 'nansu'

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.filter(nansu=self.kwargs[self.lookup_field]).first()
        if not obj:
            raise Http404(f"No {self.lookup_field} matching the query")
        return obj

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        nansu = request.data.get('nansu')
        if nansu and nansu != instance.nansu:
            raise serializers.ValidationError("Invalid value for 'nansu'")
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(pic=serializer.validated_data['pic'])


class JulyFrontPutView(generics.UpdateAPIView):
    serializer_class = JulyFrontSerializer
    queryset = JulyFront.objects.all()
    lookup_field = 'nansu'

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.filter(nansu=self.kwargs[self.lookup_field]).first()
        if not obj:
            raise Http404(f"No {self.lookup_field} matching the query")
        return obj

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        nansu = request.data.get('nansu')
        if nansu and nansu != instance.nansu:
            raise serializers.ValidationError("Invalid value for 'nansu'")
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(pic=serializer.validated_data['pic'])


class JulyBackPutView(generics.UpdateAPIView):
    serializer_class = JulyBackSerializer
    queryset = JulyBack.objects.all()
    lookup_field = 'nansu'

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.filter(nansu=self.kwargs[self.lookup_field]).first()
        if not obj:
            raise Http404(f"No {self.lookup_field} matching the query")
        return obj

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        nansu = request.data.get('nansu')
        if nansu and nansu != instance.nansu:
            raise serializers.ValidationError("Invalid value for 'nansu'")
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(pic=serializer.validated_data['pic'])

class AugFrontPutView(generics.UpdateAPIView):
    serializer_class = AugFrontSerializer
    queryset = AugFront.objects.all()
    lookup_field = 'nansu'

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.filter(nansu=self.kwargs[self.lookup_field]).first()
        if not obj:
            raise Http404(f"No {self.lookup_field} matching the query")
        return obj

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        nansu = request.data.get('nansu')
        if nansu and nansu != instance.nansu:
            raise serializers.ValidationError("Invalid value for 'nansu'")
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(pic=serializer.validated_data['pic'])


class AugBackPutView(generics.UpdateAPIView):
    serializer_class = AugBackSerializer
    queryset = AugBack.objects.all()
    lookup_field = 'nansu'

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.filter(nansu=self.kwargs[self.lookup_field]).first()
        if not obj:
            raise Http404(f"No {self.lookup_field} matching the query")
        return obj

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        nansu = request.data.get('nansu')
        if nansu and nansu != instance.nansu:
            raise serializers.ValidationError("Invalid value for 'nansu'")
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(pic=serializer.validated_data['pic'])


class SepFrontPutView(generics.UpdateAPIView):
    serializer_class = SepFrontSerializer
    queryset = SepFront.objects.all()
    lookup_field = 'nansu'

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.filter(nansu=self.kwargs[self.lookup_field]).first()
        if not obj:
            raise Http404(f"No {self.lookup_field} matching the query")
        return obj

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        nansu = request.data.get('nansu')
        if nansu and nansu != instance.nansu:
            raise serializers.ValidationError("Invalid value for 'nansu'")
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(pic=serializer.validated_data['pic'])


class SepBackPutView(generics.UpdateAPIView):
    serializer_class = SepBackSerializer
    queryset = SepBack.objects.all()
    lookup_field = 'nansu'

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.filter(nansu=self.kwargs[self.lookup_field]).first()
        if not obj:
            raise Http404(f"No {self.lookup_field} matching the query")
        return obj

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        nansu = request.data.get('nansu')
        if nansu and nansu != instance.nansu:
            raise serializers.ValidationError("Invalid value for 'nansu'")
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(pic=serializer.validated_data['pic'])


class OctFrontPutView(generics.UpdateAPIView):
    serializer_class = OctFrontSerializer
    queryset = OctFront.objects.all()
    lookup_field = 'nansu'

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.filter(nansu=self.kwargs[self.lookup_field]).first()
        if not obj:
            raise Http404(f"No {self.lookup_field} matching the query")
        return obj

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        nansu = request.data.get('nansu')
        if nansu and nansu != instance.nansu:
            raise serializers.ValidationError("Invalid value for 'nansu'")
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(pic=serializer.validated_data['pic'])


class OctBackPutView(generics.UpdateAPIView):
    serializer_class = OctBackSerializer
    queryset = OctBack.objects.all()
    lookup_field = 'nansu'

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.filter(nansu=self.kwargs[self.lookup_field]).first()
        if not obj:
            raise Http404(f"No {self.lookup_field} matching the query")
        return obj

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        nansu = request.data.get('nansu')
        if nansu and nansu != instance.nansu:
            raise serializers.ValidationError("Invalid value for 'nansu'")
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(pic=serializer.validated_data['pic'])


class NovFrontPutView(generics.UpdateAPIView):
    serializer_class = NovFrontSerializer
    queryset = NovFront.objects.all()
    lookup_field = 'nansu'

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.filter(nansu=self.kwargs[self.lookup_field]).first()
        if not obj:
            raise Http404(f"No {self.lookup_field} matching the query")
        return obj

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        nansu = request.data.get('nansu')
        if nansu and nansu != instance.nansu:
            raise serializers.ValidationError("Invalid value for 'nansu'")
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(pic=serializer.validated_data['pic'])


class NovBackPutView(generics.UpdateAPIView):
    serializer_class = NovBackSerializer
    queryset = NovBack.objects.all()
    lookup_field = 'nansu'

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.filter(nansu=self.kwargs[self.lookup_field]).first()
        if not obj:
            raise Http404(f"No {self.lookup_field} matching the query")
        return obj

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        nansu = request.data.get('nansu')
        if nansu and nansu != instance.nansu:
            raise serializers.ValidationError("Invalid value for 'nansu'")
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(pic=serializer.validated_data['pic'])


class DecFrontPutView(generics.UpdateAPIView):
    serializer_class = DecFrontSerializer
    queryset = DecFront.objects.all()
    lookup_field = 'nansu'

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.filter(nansu=self.kwargs[self.lookup_field]).first()
        if not obj:
            raise Http404(f"No {self.lookup_field} matching the query")
        return obj

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        nansu = request.data.get('nansu')
        if nansu and nansu != instance.nansu:
            raise serializers.ValidationError("Invalid value for 'nansu'")
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(pic=serializer.validated_data['pic'])


class DecBackPutView(generics.UpdateAPIView):
    serializer_class = DecBackSerializer
    queryset = DecBack.objects.all()
    lookup_field = 'nansu'

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.filter(nansu=self.kwargs[self.lookup_field]).first()
        if not obj:
            raise Http404(f"No {self.lookup_field} matching the query")
        return obj

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        nansu = request.data.get('nansu')
        if nansu and nansu != instance.nansu:
            raise serializers.ValidationError("Invalid value for 'nansu'")
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(pic=serializer.validated_data['pic'])


class PrologPutView(generics.UpdateAPIView):
    serializer_class = PrologSerializer
    queryset = Prolog.objects.all()
    lookup_field = 'nansu'

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.filter(nansu=self.kwargs[self.lookup_field]).first()
        if not obj:
            raise Http404(f"No {self.lookup_field} matching the query")
        return obj

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        nansu = request.data.get('nansu')
        if nansu and nansu != instance.nansu:
            raise serializers.ValidationError("Invalid value for 'nansu'")
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(pic=serializer.validated_data['pic'])


class CoverPutView(generics.UpdateAPIView):
    serializer_class = CoverSerializer
    queryset = Cover.objects.all()
    lookup_field = 'nansu'

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.filter(nansu=self.kwargs[self.lookup_field]).first()
        if not obj:
            raise Http404(f"No {self.lookup_field} matching the query")
        return obj

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        nansu = request.data.get('nansu')
        if nansu and nansu != instance.nansu:
            raise serializers.ValidationError("Invalid value for 'nansu'")
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(pic=serializer.validated_data['pic'])


def nansu_info_detail(request, info_seq, nansu_count):
    nansu_list = Nansu.objects.all()[:nansu_count]
    context = {'nansu_list': nansu_list}
    return render(request, 'app/nansu_info_detail.html', context)


class NansuList(APIView):
    @swagger_auto_schema(
        operation_summary='난수 전체 리스트 GET API',
    )
    def get(self, request):
        nansuData = Nansu.objects.all()
        serializers = NansuSerializer(nansuData, many=True)
        return Response(serializers.data)

class OrderList(APIView): #주문 버튼을 누를때 Update
    @swagger_auto_schema(
        operation_summary='주문자 정보 전체 리스트 GET API',
    )
    def get(self, request):
        orderData = Order.objects.all()
        serializers = OrderSerializer(orderData, many=True)
        return Response(serializers.data)

class OrderInfoList(APIView):
    @swagger_auto_schema(
        operation_summary='주문상태 리스트 GET API(미주문, 주문신청, 주문완료)',
    )
    def get(self, request):
        nansuInfoData = OrderInfo.objects.all()
        serializers = OrderInfoSerializer(nansuInfoData, many=True)
        return Response(serializers.data)

class CalendarList(APIView):
    @swagger_auto_schema(
        operation_summary='달력 정보 전체 리스트 GET API',
    )
    def get(self, request):
        calendarData = Calendar.objects.all()
        serializers = CalendarSerializer(calendarData, many=True)
        return Response(serializers.data)
    def post(self, request):
        serializer = CalendarSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     


class NoticeDeleteView(generics.DestroyAPIView):
    serializer_class = NoticeSerializer
    lookup_field = 'nansu'

    def get_queryset(self):
        queryset = Notice.objects.all()
        nansu = self.request.data.get('nansu')
        monthdays = self.request.data.get('monthdays')
        if nansu:
            queryset = queryset.filter(nansu=nansu)
        if monthdays:
            queryset = queryset.filter(monthdays=monthdays)
        return queryset

    @swagger_auto_schema(
        operation_summary='메모 DELETE API',
        request_body=NoticeSerializer
    )
    def delete(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({"detail": "해당하는 데이터가 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

        instance = queryset.first()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


class NoticePutView(generics.UpdateAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    lookup_field = 'nansu'

    def get_object(self):
        nansu = self.request.data.get('nansu')
        monthdays = self.request.data.get('monthdays')
        queryset = self.get_queryset().filter(nansu=nansu, monthdays=monthdays)
        obj = queryset.first()
        if obj is None:
            raise Http404("No object matching given query.")
        return obj

    @swagger_auto_schema(
        operation_summary='메모 PUT API',
        #request_body=NoticeSerializer
    )
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        nansu = request.data.get('nansu')
        monthdays = request.data.get('monthdays')

        if nansu and nansu != instance.nansu:
            raise serializers.ValidationError("Invalid value for 'nansu'")
        if monthdays and monthdays != instance.monthdays:
            raise serializers.ValidationError("Invalid value for 'monthdays'")

        partial = kwargs.pop('partial', False)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()


class NoticePostView(generics.CreateAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer

    @swagger_auto_schema(
        operation_summary='메모 POST API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class NoticeListView(generics.ListCreateAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        nansu = self.request.query_params.get('nansu')
        if nansu is not None:
            queryset = queryset.filter(nansu__exact=nansu)
        return queryset

    @swagger_auto_schema(
        operation_summary='메모 GET API',
        query_serializer=NoticeSerializer
    )
    def get(self, request, *args, **kwargs):
        query_params_serializer = NoticeSerializer(data=request.query_params)
        query_params_serializer.is_valid(raise_exception=True)
        nansu = request.query_params.get('nansu', None)

        #nansu = query_params_serializer.validated_data.get('nansu')

        filtered_queryset = self.get_queryset().filter(nansu=nansu)
        print(filtered_queryset)

        if not filtered_queryset.exists():
            return Response({"detail": "해당하는 데이터가 존재하지 않습니다."})

        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(serializer.data)


class JanFront(generics.ListCreateAPIView):
    queryset = JanFront.objects.all()
    serializer_class = JanFrontSerializer


    @swagger_auto_schema(
        operation_summary='1월 앞 POST API',
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary='1월 앞 GET API',
        query_serializer=JanFrontSerializer
    )
    def get(self, request, *args, **kwargs):
        query_params_serializer = JanFrontSerializer(data=request.query_params)
        query_params_serializer.is_valid(raise_exception=True)
        nansu = query_params_serializer.validated_data.get('nansu')

        filtered_queryset = self.queryset.filter(nansu=nansu)
        print(filtered_queryset)
        
        if not filtered_queryset.exists():
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."})

        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(serializer.data)


class JanBack(generics.ListCreateAPIView):
    serializer_class = JanBackSerializer
    queryset = JanBack.objects.all()

    @swagger_auto_schema(
        operation_summary='1월 뒤 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='1월 뒤 GET API',
        query_serializer=JanBackSerializer
    )
    def get(self, request, *args, **kwargs):
        query_params_serializer = JanBackSerializer(data=request.query_params)
        query_params_serializer.is_valid(raise_exception=True)
        nansu = query_params_serializer.validated_data.get('nansu')
        pic = query_params_serializer.validated_data.get('pic')
        print(pic)
        filtered_queryset = self.queryset.filter(nansu=nansu)
        
        if not filtered_queryset.exists():
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."})

        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(serializer.data)




class FebFront(generics.ListCreateAPIView):
    serializer_class = FebFrontSerializer
    queryset = FebFront.objects.all()

    @swagger_auto_schema(
        operation_summary='2월 앞 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='2월 앞 GET API',
        query_serializer=FebBackSerializer
    )
    def get(self, request, *args, **kwargs):
        query_params_serializer = FebBackSerializer(data=request.query_params)
        query_params_serializer.is_valid(raise_exception=True)
        nansu = query_params_serializer.validated_data.get('nansu')

        filtered_queryset = self.queryset.filter(nansu=nansu)
        
        if not filtered_queryset.exists():
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."})

        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(serializer.data)

class FebBack(generics.ListCreateAPIView):
    serializer_class = FebBackSerializer
    queryset = FebBack.objects.all()

    @swagger_auto_schema(
        operation_summary='2월 뒤 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='2월 뒤 GET API',
        query_serializer=FebBackSerializer
    )
    def get(self, request, *args, **kwargs):
        query_params_serializer = FebBackSerializer(data=request.query_params)
        query_params_serializer.is_valid(raise_exception=True)
        nansu = query_params_serializer.validated_data.get('nansu')

        filtered_queryset = self.queryset.filter(nansu=nansu)
        
        if not filtered_queryset.exists():
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."})

        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(serializer.data)




class MarFront(generics.ListCreateAPIView):
    serializer_class = MarFrontSerializer
    queryset = MarFront.objects.all()

    @swagger_auto_schema(
        operation_summary='3월 앞 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='3월 앞 GET API',
        query_serializer=MarFrontSerializer
    )
    def get(self, request, *args, **kwargs):
        query_params_serializer = MarFrontSerializer(data=request.query_params)
        query_params_serializer.is_valid(raise_exception=True)
        nansu = query_params_serializer.validated_data.get('nansu')

        filtered_queryset = self.queryset.filter(nansu=nansu)
        
        if not filtered_queryset.exists():
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."})

        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(serializer.data)


class MarBack(generics.ListCreateAPIView):
    serializer_class = MarBackSerializer
    queryset = MarBack.objects.all()

    @swagger_auto_schema(
        operation_summary='3월 뒤 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='3월 뒤 GET API',
        query_serializer=MarBackSerializer
    )
    def get(self, request, *args, **kwargs):
        query_params_serializer = MarBackSerializer(data=request.query_params)
        query_params_serializer.is_valid(raise_exception=True)
        nansu = query_params_serializer.validated_data.get('nansu')

        filtered_queryset = self.queryset.filter(nansu=nansu)
        
        if not filtered_queryset.exists():
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."})

        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(serializer.data)



class AprilFront(generics.ListCreateAPIView):
    serializer_class = AprilFrontSerializer
    queryset = AprilFront.objects.all()

    @swagger_auto_schema(
        operation_summary='4월 앞 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='4월 앞 GET API',
        query_serializer=AprilFrontSerializer
    )
    def get(self, request, *args, **kwargs):
        query_params_serializer = AprilFrontSerializer(data=request.query_params)
        query_params_serializer.is_valid(raise_exception=True)
        nansu = query_params_serializer.validated_data.get('nansu')

        filtered_queryset = self.queryset.filter(nansu=nansu)
        
        if not filtered_queryset.exists():
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."})

        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(serializer.data)


class AprilBack(generics.ListCreateAPIView):
    serializer_class = AprilBackSerializer
    queryset = AprilBack.objects.all()

    @swagger_auto_schema(
        operation_summary='4월 뒤 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='4월 뒤 GET API',
        query_serializer=AprilBackSerializer
    )
    def get(self, request, *args, **kwargs):
        query_params_serializer = AprilBackSerializer(data=request.query_params)
        query_params_serializer.is_valid(raise_exception=True)
        nansu = query_params_serializer.validated_data.get('nansu')

        filtered_queryset = self.queryset.filter(nansu=nansu)
        
        if not filtered_queryset.exists():
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."})

        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(serializer.data)



class MayFront(generics.ListCreateAPIView):
    serializer_class = MayFrontSerializer
    queryset = MayFront.objects.all()

    @swagger_auto_schema(
        operation_summary='5월 앞 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='5월 앞 GET API',
        query_serializer=MayFrontSerializer
    )
    def get(self, request, *args, **kwargs):
        query_params_serializer = MayFrontSerializer(data=request.query_params)
        query_params_serializer.is_valid(raise_exception=True)
        nansu = query_params_serializer.validated_data.get('nansu')

        filtered_queryset = self.queryset.filter(nansu=nansu)
        
        if not filtered_queryset.exists():
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."})

        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(serializer.data)


class MayBack(generics.ListCreateAPIView):
    serializer_class = MayBackSerializer
    queryset = MayBack.objects.all()

    @swagger_auto_schema(
        operation_summary='5월 뒤 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='5월 뒤 GET API',
        query_serializer=MayBackSerializer
    )
    def get(self, request, *args, **kwargs):
        query_params_serializer = MayBackSerializer(data=request.query_params)
        query_params_serializer.is_valid(raise_exception=True)
        nansu = query_params_serializer.validated_data.get('nansu')

        filtered_queryset = self.queryset.filter(nansu=nansu)
        
        if not filtered_queryset.exists():
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."})

        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(serializer.data)




class JuneFront(generics.ListCreateAPIView):
    serializer_class = JuneFrontSerializer
    queryset = JuneFront.objects.all()

    @swagger_auto_schema(
        operation_summary='6월 앞 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='6월 앞 GET API',
        query_serializer=JuneFrontSerializer
    )
    def get(self, request, *args, **kwargs):
        query_params_serializer = JuneFrontSerializer(data=request.query_params)
        query_params_serializer.is_valid(raise_exception=True)
        nansu = query_params_serializer.validated_data.get('nansu')

        filtered_queryset = self.queryset.filter(nansu=nansu)
        
        if not filtered_queryset.exists():
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."})

        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(serializer.data)


class JuneBack(generics.ListCreateAPIView):
    serializer_class = JuneBackSerializer
    queryset = JuneBack.objects.all()

    @swagger_auto_schema(
        operation_summary='6월 뒤 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='6월 뒤 GET API',
        query_serializer=JuneBackSerializer
    )
    def get(self, request, *args, **kwargs):
        query_params_serializer = JuneBackSerializer(data=request.query_params)
        query_params_serializer.is_valid(raise_exception=True)
        nansu = query_params_serializer.validated_data.get('nansu')

        filtered_queryset = self.queryset.filter(nansu=nansu)
        
        if not filtered_queryset.exists():
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."})

        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(serializer.data)




class JulyFront(generics.ListCreateAPIView):
    serializer_class = JulyFrontSerializer
    queryset = JulyFront.objects.all()

    @swagger_auto_schema(
        operation_summary='7월 앞 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='7월 앞 GET API',
        query_serializer=JulyFrontSerializer
    )
    def get(self, request, *args, **kwargs):
        query_params_serializer = JulyFrontSerializer(data=request.query_params)
        query_params_serializer.is_valid(raise_exception=True)
        nansu = query_params_serializer.validated_data.get('nansu')

        filtered_queryset = self.queryset.filter(nansu=nansu)
        
        if not filtered_queryset.exists():
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."})

        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(serializer.data)


class JulyBack(generics.ListCreateAPIView):
    serializer_class = JulyBackSerializer
    queryset = JulyBack.objects.all()

    @swagger_auto_schema(
        operation_summary='7월 뒤 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='7월 뒤 GET API',
        query_serializer=JulyBackSerializer
    )
    def get(self, request, *args, **kwargs):
        query_params_serializer = JulyBackSerializer(data=request.query_params)
        query_params_serializer.is_valid(raise_exception=True)
        nansu = query_params_serializer.validated_data.get('nansu')

        filtered_queryset = self.queryset.filter(nansu=nansu)
        
        if not filtered_queryset.exists():
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."})

        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(serializer.data)




class AugFront(generics.ListCreateAPIView):
    serializer_class = AugFrontSerializer
    queryset = AugFront.objects.all()

    @swagger_auto_schema(
        operation_summary='8월 앞 POST API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='8월 앞 GET API',
        query_serializer=AugFrontSerializer
    )
    def get(self, request, *args, **kwargs):
        query_params_serializer = AugFrontSerializer(data=request.query_params)
        query_params_serializer.is_valid(raise_exception=True)
        nansu = query_params_serializer.validated_data.get('nansu')

        filtered_queryset = self.queryset.filter(nansu=nansu)
        
        if not filtered_queryset.exists():
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."})

        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(serializer.data)


class AugBack(generics.ListCreateAPIView):
    serializer_class = AugBackSerializer
    queryset = AugBack.objects.all()

    @swagger_auto_schema(
        operation_summary='8월 뒤 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='8월 뒤 GET API',
        query_serializer=AugBackSerializer
    )
    def get(self, request, *args, **kwargs):
        query_params_serializer = AugBackSerializer(data=request.query_params)
        query_params_serializer.is_valid(raise_exception=True)
        nansu = query_params_serializer.validated_data.get('nansu')

        filtered_queryset = self.queryset.filter(nansu=nansu)
        
        if not filtered_queryset.exists():
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."})

        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(serializer.data)




class SepFront(generics.ListCreateAPIView):
    serializer_class = SepFrontSerializer
    queryset = SepFront.objects.all()

    @swagger_auto_schema(
        operation_summary='9월 앞 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='9월 앞 GET API',
        query_serializer=SepFrontSerializer
    )
    def get(self, request, *args, **kwargs):
        query_params_serializer = SepFrontSerializer(data=request.query_params)
        query_params_serializer.is_valid(raise_exception=True)
        nansu = query_params_serializer.validated_data.get('nansu')

        filtered_queryset = self.queryset.filter(nansu=nansu)
        
        if not filtered_queryset.exists():
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."})

        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(serializer.data)


class SepBack(generics.ListCreateAPIView):
    serializer_class = SepBackSerializer
    queryset = SepBack.objects.all()

    @swagger_auto_schema(
        operation_summary='9월 뒤 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='9월 뒤 GET API',
        query_serializer=SepBackSerializer
    )
    def get(self, request, *args, **kwargs):
        query_params_serializer = SepBackSerializer(data=request.query_params)
        query_params_serializer.is_valid(raise_exception=True)
        nansu = query_params_serializer.validated_data.get('nansu')

        filtered_queryset = self.queryset.filter(nansu=nansu)
        
        if not filtered_queryset.exists():
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."})

        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(serializer.data)




class OctFront(generics.ListCreateAPIView):
    serializer_class = OctFrontSerializer
    queryset = OctFront.objects.all()

    @swagger_auto_schema(
        operation_summary='10월 앞 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='10월 뒤 GET API',
        query_serializer=OctFrontSerializer
    )
    def get(self, request, *args, **kwargs):
        query_params_serializer = OctFrontSerializer(data=request.query_params)
        query_params_serializer.is_valid(raise_exception=True)
        nansu = query_params_serializer.validated_data.get('nansu')

        filtered_queryset = self.queryset.filter(nansu=nansu)
        
        if not filtered_queryset.exists():
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."})

        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(serializer.data)


class OctBack(generics.ListCreateAPIView):
    serializer_class = OctBackSerializer
    queryset = OctBack.objects.all()

    @swagger_auto_schema(
        operation_summary='10월 뒤 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='10월 뒤 GET API',
        query_serializer=OctBackSerializer
    )
    def get(self, request, *args, **kwargs):
        query_params_serializer = OctBackSerializer(data=request.query_params)
        query_params_serializer.is_valid(raise_exception=True)
        nansu = query_params_serializer.validated_data.get('nansu')

        filtered_queryset = self.queryset.filter(nansu=nansu)
        
        if not filtered_queryset.exists():
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."})

        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(serializer.data)




class NovFront(generics.ListCreateAPIView):
    serializer_class = NovFrontSerializer
    queryset = NovFront.objects.all()

    @swagger_auto_schema(
        operation_summary='11월 앞 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='11월 앞 GET API',
        query_serializer=NovFrontSerializer
    )
    def get(self, request, *args, **kwargs):
        query_params_serializer = NovFrontSerializer(data=request.query_params)
        query_params_serializer.is_valid(raise_exception=True)
        nansu = query_params_serializer.validated_data.get('nansu')

        filtered_queryset = self.queryset.filter(nansu=nansu)
        
        if not filtered_queryset.exists():
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."})

        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(serializer.data)


class NovBack(generics.ListCreateAPIView):
    serializer_class = NovBackSerializer
    queryset = NovBack.objects.all()

    @swagger_auto_schema(
        operation_summary='11월 뒤 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='11월 뒤 GET API',
        query_serializer=NovBackSerializer
    )
    def get(self, request, *args, **kwargs):
        query_params_serializer = NovBackSerializer(data=request.query_params)
        query_params_serializer.is_valid(raise_exception=True)
        nansu = query_params_serializer.validated_data.get('nansu')

        filtered_queryset = self.queryset.filter(nansu=nansu)
        
        if not filtered_queryset.exists():
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."})

        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(serializer.data)




class DecFront(generics.ListCreateAPIView):
    serializer_class = DecFrontSerializer
    queryset = DecFront.objects.all()

    @swagger_auto_schema(
        operation_summary='12월 앞 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='12월 앞 GET API',
        query_serializer=DecFrontSerializer
    )
    def get(self, request, *args, **kwargs):
        query_params_serializer = DecFrontSerializer(data=request.query_params)
        query_params_serializer.is_valid(raise_exception=True)
        nansu = query_params_serializer.validated_data.get('nansu')

        filtered_queryset = self.queryset.filter(nansu=nansu)
        
        if not filtered_queryset.exists():
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."})

        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(serializer.data)


class DecBack(generics.ListCreateAPIView):
    serializer_class = DecBackSerializer
    queryset = DecBack.objects.all()

    @swagger_auto_schema(
        operation_summary='12월 뒤 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='12월 뒤 GET API',
        query_serializer=DecBackSerializer
    )
    def get(self, request, *args, **kwargs):
        query_params_serializer = DecBackSerializer(data=request.query_params)
        query_params_serializer.is_valid(raise_exception=True)
        nansu = query_params_serializer.validated_data.get('nansu')

        filtered_queryset = self.queryset.filter(nansu=nansu)
        
        if not filtered_queryset.exists():
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."})

        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(serializer.data)




class Prolog(generics.ListCreateAPIView):
    serializer_class = PrologSerializer
    queryset = Prolog.objects.all()

    @swagger_auto_schema(
        operation_summary='프롤로그2 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='프롤로그2 GET API',
        query_serializer=PrologSerializer
    )
    def get(self, request, *args, **kwargs):
        query_params_serializer = PrologSerializer(data=request.query_params)
        query_params_serializer.is_valid(raise_exception=True)
        nansu = query_params_serializer.validated_data.get('nansu')

        filtered_queryset = self.queryset.filter(nansu=nansu)
        
        if not filtered_queryset.exists():
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."})

        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(serializer.data)



class Cover(generics.ListCreateAPIView):
    serializer_class = CoverSerializer
    queryset = Cover.objects.all()

    @swagger_auto_schema(
        operation_summary='프롤로그1 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_summary='프롤로그2 GET API',
        query_serializer=CoverSerializer
    )
    def get(self, request, *args, **kwargs):
        query_params_serializer = CoverSerializer(data=request.query_params)
        query_params_serializer.is_valid(raise_exception=True)
        nansu = query_params_serializer.validated_data.get('nansu')

        filtered_queryset = self.queryset.filter(nansu=nansu)
        
        if not filtered_queryset.exists():
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."})

        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(serializer.data)



#@csrf_exempt
class NansuUrlDetail(APIView):
    def get_object(self, nansu):#GET,PUT,DELETE
        try:
            return Nansu.objects.get(nansu=nansu)
        except Nansu.DoesNotExist:
            raise Http404
    @swagger_auto_schema(
        operation_summary='난수 정보(입력란에 난수를 입력하시면 됩니다.)',
    )
    def get(self, request, nansu):
        nansuUrl = self.get_object(nansu)
        serializer = NansuSerializer(nansuUrl)
        return Response(serializer.data)

    @swagger_auto_schema( #Nansu POST API 성공.
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'nansu_seq': openapi.Schema(type=openapi.TYPE_INTEGER, description='정수타입', required=['nansu_seq'])
            },#properties에서 ORM하면 됨. 'nansu','nansu_state','permission' 컬럼 추가 가능.
        ),
            responses={
                400: '에러',
                201: '작성된 리소스 정보'
            },
            operation_summary='난수 리소스 생성 API',
            operation_description='난수 리소스를 생성하는 API입니다.'
        )
    def post(self, request, nansu):
        serializer = NansuSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@renderer_classes([SwaggerUIRenderer])
class SwaggerSchemaView(APIView):
    def get(self, request):
        schema_url = reverse('schema-json')
        extra_forms = [
            {
                "name": "file",
                "in": "formData",
                "required": True,
                "type": "file"
            }
        ]
        return Response(
            {
                "openapi": "3.0.0",
                "info": {"title": "My API", "version": "1.0.0"},
                "paths": {},
                "components": {"schemas": {}},
                "x-extra-forms": extra_forms,
            },
            template_name="swagger-ui.html",
        )

class ImageView(generics.CreateAPIView):
    parser_classes = (MultiPartParser,)
    serializer_class = ImageSerializer

    @swagger_auto_schema(
            operation_summary='이미지 POST API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

        

class OrderUrlDetail(generics.CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class CalendarUrlDetail(APIView):
    @swagger_auto_schema(
            operation_summary='달력 세부 정보',
        )
    def get_object(self, calendar):
        try:
            return Calendar.objects.prefetch_related('nansu').get(calendar_seq=calendar)
        except Calendar.DoesNotExist:
            raise Http404

    def get(self, request, calendar):
        calendar_url = self.get_object(calendar)
        serializer = CalendarSerializer(calendar_url)
        nansu_serializer = NansuSerializer(calendar_url.nansu)
        response_data = serializer.data
        response_data['nansu'] = nansu_serializer.data
        return Response(response_data)

    def post(self, request, calendar):
        serializer = Serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

