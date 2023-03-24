from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import ListView, DetailView
from rest_framework_swagger.renderers import SwaggerUIRenderer
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

def index(request):
    return HttpResponse("TEST PAGE")


class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        # 세션 데이터 백업
        session_backup = dict(request.session)

        # 로그아웃
        response = super().dispatch(request, *args, **kwargs)

        # 백업된 세션 데이터를 복원
        for key, value in session_backup.items():
            request.session[key] = value

        return response

def nansu_info_detail(request, info_seq, nansu_count):
    nansu_list = Nansu.objects.all()[:nansu_count]
    context = {'nansu_list': nansu_list}
    return render(request, 'app/nansu_info_detail.html', context)


def nansu(request):
    nansuTest = Nansu.objects.filter(nansu_state='정상')
    print(nansuTest)
    return render(request,'index.html', {"nansuTest":nansuTest})

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

class MonthAPI2(generics.CreateAPIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'jan_seq': openapi.Schema(type=openapi.TYPE_INTEGER, description='정수타입',required=['jan_seq']),
            },
        ),
        responses={
            400: '에러',
            201: '작성된 리소스 정보'
        },
        operation_summary='월별 리소스 생성 API',
        operation_description='월별 리소스를 생성하는 API입니다. month 쿼리 매개변수에는 month 값 중 하나를 지정해야 합니다.'
    )
    def post(self, request):
        jan_front_serializer = JanFrontSerializer(data=request.data)
        jan_back_serializer = JanBackSerializer(data=request.data)
        feb_front_serializer = FebFrontSerializer(data=request.data)
        feb_back_serializer = FebBackSerializer(data=request.data)
        mar_front_serializer = MarFrontSerializer(data=request.data)
        mar_back_serializer = MarBackSerializer(data=request.data)
        april_front_serializer = AprilFrontSerializer(data=request.data)
        april_back_serializer = AprilBackSerializer(data=request.data)
        june_front_serializer = JuneFrontSerializer(data=request.data)
        june_back_serializer = JuneBackSerializer(data=request.data)
        july_front_serializer = JulyFrontSerializer(data=request.data)
        july_back_serializer = JulyBackSerializer(data=request.data)
        aug_front_serializer = AugFrontSerializer(data=request.data)
        aug_back_serializer = AugBackSerializer(data=request.data)

        if jan_front_serializer.is_valid() and jan_back_serializer.is_valid() and feb_front_serializer.is_valid() and feb_back_serializer.is_valid() and mar_front_serializer.is_valid() and mar_back_serializer.is_valid() and april_front_serializer.is_valid() and april_back_serializer.is_valid() and june_front_serializer.is_valid() and june_back_serializer.is_valid() and july_front_serializer.is_valid() and july_back_serializer.is_valid() and aug_front_serializer.is_valid() and aug_back_serializer.is_valid():
            jan_front_serializer.save()
            jan_back_serializer.save()
            feb_front_serializer.save()
            feb_back_serializer.save()
            mar_front_serializer.save()
            mar_back_serializer.save()
            april_front_serializer.save()
            april_back_serializer.save()
            june_front_serializer.save()
            june_back_serializer.save()
            july_front_serializer.save()
            july_back_serializer.save()
            aug_front_serializer.save()
            aug_back_serializer.save()

            return Response("All objects created", status=status.HTTP_201_CREATED)

        else:
            return Response(jan_front_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MonthAPI(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'jan_seq': openapi.Schema(type=openapi.TYPE_INTEGER, description='정수타입',required=['jan_seq']),
            },
        ),
        responses={
            400: '에러',
            201: '작성된 리소스 정보'
        },
        operation_summary='월별 리소스 생성 API(수정중.)',
        operation_description='월별 리소스를 생성하는 API입니다. month 쿼리 매개변수에는 month 값 중 하나를 지정해야 합니다.'
    )
    def post(self, request,month):
        month = request.data.get('month', None)
        if month is None:
            return Response({'에러'}, status=status.HTTP_400_BAD_REQUEST)
        
        if month == 'jan_front':
            serializer = JanFrontSerializer(data=request.data)
            print('jan_front print')
            model = JanFront
        elif month == 'jan_back':
            serializer = JanBackSerializer(data=request.data)
            model = JanBack
        elif month == 'feb_front':
            serializer = FebFrontSerializer(data=request.data)
            model = FebFront
        elif month == 'feb_back':
            serializer = FebBackSerializer(data=request.data)
            model = FebBack
        elif month == 'mar_front':
            serializer = MarFrontSerializer(data=request.data)
            model = MarFront
        elif month == 'mar_back':
            serializer = MarBackSerializer(data=request.data)
            model = MarBack
        elif month == 'april_front':
            serializer = AprilFrontSerializer(data=request.data)
            model = AprilFront
        elif month == 'april_back':
            serializer = AprilBackSerializer(data=request.data)
            model = AprilBack
        elif month == 'may_front':
            serializer = MayFrontSerializer(data=request.data)
            model = MayFront
        elif month == 'may_back':
            serializer = MayBackSerializer(data=request.data)
            model = MayFront
        elif month == 'june_front':
            serializer = JuneFrontSerializer(data=request.data)
            model = JuneFront
        elif month == 'june_back':
            serializer = JuneBackSerializer(data=request.data)
            model = JuneBack
        elif month == 'july_front':
            serializer = JulyFrontSerializer(data=request.data)
            model = JulyFront
        elif month == 'july_back':
            serializer = JulyBackSerializer(data=request.data)
            model = JulyBack
        elif month == 'aug_front':
            serializer = AugFrontSerializer(data=request.data)
            model = AugFront
        elif month == 'aug_back':
            serializer = AugBackSerializer(data=request.data)
            model = AugBack
        elif month == 'sep_front':
            serializer = SepFrontSerializer(data=request.data)
            model = SepFront
        elif month == 'sep_back':
            serializer = SepBackSerializer(data=request.data)
            model = SepBack
        elif month == 'oct_front':
            serializer = OctFrontSerializer(data=request.data)
            model = OctFront
        elif month == 'oct_back':
            serializer = OctBackSerializer(data=request.data)
            model = OctBack
        elif month == 'nov_front':
            serializer = NovFrontSerializer(data=request.data)
            model = NovFront
        elif month == 'nov_back':
            serializer = NovBackSerializer(data=request.data)
            model = NovBack
        elif month == 'dec_front':
            serializer = DecFrontSerializer(data=request.data)
            model = DecFront
        elif month == 'dec_back':
            serializer = DecBackSerializer(data=request.data)
            model = DecBack
        elif month == 'prolog':
            serializer = PrologSerializer(data=request.data)
            model = Prolog
        elif month == 'cover':
            serializer = CoverSerializer(data=request.data)
            model = Cover
        else:
            return Response({'error': 'invalid month field.'}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class Notice(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoticeSerializer
    queryset = Notice.objects.all()

    @swagger_auto_schema(
        operation_summary='메모 POST API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary='메모 PUT API',
        request_body=NoticeSerializer,
        responses={200: NoticeSerializer}
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return Response({"detail": "DELETE 요청은 허용되지 않습니다."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def patch(self, request, *args, **kwargs):
        return Response({"detail": "PATCH 요청은 허용되지 않습니다."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @swagger_auto_schema(
        operation_summary='메모 GET API',
        query_serializer=NoticeSerializer
    )
    def get(self, request, *args, **kwargs):
        query_params_serializer = NoticeSerializer(data=request.query_params)
        query_params_serializer.is_valid(raise_exception=True)
        nansu = query_params_serializer.validated_data.get('nansu')

        filtered_queryset = self.queryset.filter(nansu=nansu)

        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(serializer.data)


class JanFront(generics.ListCreateAPIView):
    serializer_class = JanFrontSerializer
    queryset = JanFront.objects.all()

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
        
        if not filtered_queryset.exists():
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

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

        filtered_queryset = self.queryset.filter(nansu=nansu)
        
        if not filtered_queryset.exists():
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

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
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

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
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

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
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

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
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

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
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

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
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

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
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

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
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

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
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

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
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

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
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

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
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

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
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

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
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

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
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

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
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

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
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

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
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

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
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

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
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

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
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

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
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

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
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

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
            return Response({"detail": "해당 nansu 값이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

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
    # def get_queryset(self):
    #     return self.serializer_class.Meta.model.objects.all()

# class ImageView(generics.CreateAPIView): #이미지 POST API

#     parser_classes = [MultiPartParser, FormParser]
#     serializer_class = ImageSerializer
#     queryset = Image.objects.all()


class OrderUrlDetail(generics.CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class CalendarUrlDetail(APIView):
    @swagger_auto_schema( #Nansu POST API 성공.
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

