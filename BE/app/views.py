from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view #api
from rest_framework import status, generics
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Nansu, Order, OrderInfo, Calendar, JanFront, JanBack, FebFront, FebBack, MarFront, MarBack, AprilFront, AprilBack, MayFront, MayBack, JuneFront, JuneBack, JulyFront, JulyBack, AugFront, AugBack, SepFront, SepBack, OctFront, OctBack, NovFront, NovBack, DecFront, DecBack, Prolog, Cover
from .serializers import NansuSerializer, OrderSerializer, OrderInfoSerializer, CalendarSerializer, JanFrontSerializer, JanBackSerializer, FebFrontSerializer, FebBackSerializer, MarFrontSerializer, MarBackSerializer,AprilFrontSerializer,AprilBackSerializer,MayFrontSerializer,MayBackSerializer, JuneFrontSerializer, JuneBackSerializer, JulyFrontSerializer, JulyBackSerializer, AugFrontSerializer, AugBackSerializer, SepFrontSerializer, SepBackSerializer, OctFrontSerializer, OctBackSerializer, NovFrontSerializer, NovBackSerializer, DecFrontSerializer, DecBackSerializer, PrologSerializer, CoverSerializer, ImageSerializer

def index(request):
    return HttpResponse("TEST PAGE")

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
        operation_summary='달력 정보 전체 리스트 GET API(Nansu테이블 nansu컬럼 매핑 작업중입니다.메모필드도 추가 예정.)',
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


class JanFront(generics.CreateAPIView):
    serializer_class = JanFrontSerializer
    queryset = JanFront.objects.all()

    @swagger_auto_schema(
        operation_summary='1월 앞 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)



class JanBack(generics.CreateAPIView):
    serializer_class = JanBackSerializer
    queryset = JanBack.objects.all()

    @swagger_auto_schema(
        operation_summary='1월 뒤 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    # def get_object(self):
    #     janBack = JanBack.objects.filter(jan_seq=self.kwargs.get('jan_back')).first()
    #     if not janBack:
    #         raise Http404
    #     return janBack

class FebFront(generics.CreateAPIView):
    serializer_class = FebFrontSerializer
    queryset = FebFront.objects.all()

    @swagger_auto_schema(
        operation_summary='2월 앞 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    # def get_object(self):
    #     febFront = FebFront.objects.filter(feb_seq=self.kwargs.get('feb_front')).first()
    #     if not febFront:
    #         raise Http404
    #     return febFront

class FebBack(generics.CreateAPIView):
    serializer_class = FebBackSerializer
    queryset = FebBack.objects.all()

    @swagger_auto_schema(
        operation_summary='2월 뒤 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    # def get_object(self):
    #     febBack = FebBack.objects.filter(feb_seq=self.kwargs.get('feb_back')).first()
    #     if not febBack:
    #         raise Http404
    #     return febBack

class MarFront(generics.CreateAPIView):
    serializer_class = MarFrontSerializer
    queryset = MarFront.objects.all()

    @swagger_auto_schema(
        operation_summary='3월 앞 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    # def get_object(self):
    #     marFront = MarFront.objects.filter(mar_seq=self.kwargs.get('mar_front')).first()
    #     if not marFront:
    #         raise Http404
    #     return marFront

class MarBack(generics.CreateAPIView):
    serializer_class = MarBackSerializer
    queryset = MarBack.objects.all()

    @swagger_auto_schema(
        operation_summary='3월 뒤 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    # def get_object(self):
    #     marBack = MarBack.objects.filter(mar_seq=self.kwargs.get('mar_back')).first()
    #     if not marBack:
    #         raise Http404
    #     return marBack

class AprilFront(generics.CreateAPIView):
    serializer_class = AprilFrontSerializer
    queryset = AprilFront.objects.all()

    @swagger_auto_schema(
        operation_summary='4월 앞 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    # def get_object(self):
    #     aprilFront = AprilFront.objects.filter(april_seq=self.kwargs.get('april_front')).first()
    #     if not aprilFront:
    #         raise Http404
    #     return aprilFront

class AprilBack(generics.CreateAPIView):
    serializer_class = AprilBackSerializer
    queryset = AprilBack.objects.all()

    @swagger_auto_schema(
        operation_summary='4월 뒤 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    # def get_object(self):
    #     aprilBack = AprilBack.objects.filter(april_seq=self.kwargs.get('april_back')).first()
    #     if not aprilBack:
    #         raise Http404
    #     return aprilBack

class MayFront(generics.CreateAPIView):
    serializer_class = MayFrontSerializer
    queryset = MayFront.objects.all()

    @swagger_auto_schema(
        operation_summary='5월 앞 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    # def get_object(self):
    #     mayFront = MayFront.objects.filter(may_seq=self.kwargs.get('may_front')).first()
    #     if not mayFront:
    #         raise Http404
    #     return mayFront

class MayBack(generics.CreateAPIView):
    serializer_class = MayBackSerializer
    queryset = MayBack.objects.all()

    @swagger_auto_schema(
        operation_summary='5월 뒤 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    # def get_object(self):
    #     mayBack = MayBack.objects.filter(may_seq=self.kwargs.get('may_back')).first()
    #     if not mayBack:
    #         raise Http404
    #     return mayBack

class JuneFront(generics.CreateAPIView):
    serializer_class = JuneFrontSerializer
    queryset = JuneFront.objects.all()

    @swagger_auto_schema(
        operation_summary='6월 앞 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    # def get_object(self):
    #     juneFront = JuneFront.objects.filter(june_seq=self.kwargs.get('june_front')).first()
    #     if not juneFront:
    #         raise Http404
    #     return juneFront

class JuneBack(generics.CreateAPIView):
    serializer_class = JuneBackSerializer
    queryset = JuneBack.objects.all()

    @swagger_auto_schema(
        operation_summary='6월 뒤 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    # def get_object(self):
    #     juneBack = JuneBack.objects.filter(june_seq=self.kwargs.get('june_back')).first()
    #     if not juneBack:
    #         raise Http404
    #     return juneBack

class JulyFront(generics.CreateAPIView):
    serializer_class = JulyFrontSerializer
    queryset = JulyFront.objects.all()

    @swagger_auto_schema(
        operation_summary='7월 앞 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    # def get_object(self):
    #     julyFront = JulyFront.objects.filter(july_seq=self.kwargs.get('july_front')).first()
    #     if not julyFront:
    #         raise Http404
    #     return julyFront

class JulyBack(generics.CreateAPIView):
    serializer_class = JulyBackSerializer
    queryset = JulyBack.objects.all()

    @swagger_auto_schema(
        operation_summary='7월 뒤 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    # def get_object(self):
    #     julyBack = JulyBack.objects.filter(july_seq=self.kwargs.get('july_back')).first()
    #     if not julyBack:
    #         raise Http404
    #     return julyBack

class AugFront(generics.CreateAPIView):
    serializer_class = AugFrontSerializer
    queryset = AugFront.objects.all()

    @swagger_auto_schema(
        operation_summary='8월 앞 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    # def get_object(self):
    #     augFront = AugFront.objects.filter(aug_seq=self.kwargs.get('aug_front')).first()
    #     if not augFront:
    #         raise Http404
    #     return augFront

class AugBack(generics.CreateAPIView):
    serializer_class = AugBackSerializer
    queryset = AugBack.objects.all()

    @swagger_auto_schema(
        operation_summary='8월 뒤 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    # def get_object(self):
    #     augBack = AugBack.objects.filter(aug_seq=self.kwargs.get('aug_back')).first()
    #     if not augBack:
    #         raise Http404
    #     return augBack

class SepFront(generics.CreateAPIView):
    serializer_class = SepFrontSerializer
    queryset = SepFront.objects.all()

    @swagger_auto_schema(
        operation_summary='9월 앞 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    # def get_object(self):
    #     sepFront = SepFront.objects.filter(sep_seq=self.kwargs.get('sep_front')).first()
    #     if not sepFront:
    #         raise Http404
    #     return sepFront

class SepBack(generics.CreateAPIView):
    serializer_class = SepBackSerializer
    queryset = SepBack.objects.all()

    @swagger_auto_schema(
        operation_summary='9월 뒤 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    # def get_object(self):
    #     sepBack = SepBack.objects.filter(sep_seq=self.kwargs.get('sep_back')).first()
    #     if not sepBack:
    #         raise Http404
    #     return sepBack

class OctFront(generics.CreateAPIView):
    serializer_class = OctFrontSerializer
    queryset = OctFront.objects.all()

    @swagger_auto_schema(
        operation_summary='10월 앞 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    # def get_object(self):
    #     octFront = OctFront.objects.filter(oct_seq=self.kwargs.get('oct_front')).first()
    #     if not octFront:
    #         raise Http404
    #     return octFront

class OctBack(generics.CreateAPIView):
    serializer_class = OctBackSerializer
    queryset = OctBack.objects.all()

    @swagger_auto_schema(
        operation_summary='10월 뒤 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    # def get_object(self):
    #     octBack = OctBack.objects.filter(oct_seq=self.kwargs.get('oct_back')).first()
    #     if not octBack:
    #         raise Http404
    #     return octBack

class NovFront(generics.CreateAPIView):
    serializer_class = NovFrontSerializer
    queryset = NovFront.objects.all()

    @swagger_auto_schema(
        operation_summary='11월 앞 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    # def get_object(self):
    #     novFront = NovFront.objects.filter(nov_seq=self.kwargs.get('nov_front')).first()
    #     if not novFront:
    #         raise Http404
    #     return aprilFrnovFrontont

class NovBack(generics.CreateAPIView):
    serializer_class = NovBackSerializer
    queryset = NovBack.objects.all()

    @swagger_auto_schema(
        operation_summary='11월 뒤 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    # def get_object(self):
    #     novBack = NovBack.objects.filter(nov_seq=self.kwargs.get('nov_back')).first()
    #     if not novBack:
    #         raise Http404
    #     return novBack

class DecFront(generics.CreateAPIView):
    serializer_class = DecFrontSerializer
    queryset = DecFront.objects.all()

    @swagger_auto_schema(
        operation_summary='12월 앞 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    # def get_object(self):
    #     decFront = DecFront.objects.filter(dec_seq=self.kwargs.get('dec_front')).first()
    #     if not decFront:
    #         raise Http404
    #     return decFront

class DecBack(generics.CreateAPIView):
    serializer_class = DecBackSerializer
    queryset = DecBack.objects.all()

    @swagger_auto_schema(
        operation_summary='12월 뒤 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    # def get_object(self):
    #     decBack = DecBack.objects.filter(dec_seq=self.kwargs.get('dec_back')).first()
    #     if not decBack:
    #         raise Http404
    #     return decBack


class Prolog(generics.CreateAPIView):
    serializer_class = PrologSerializer
    queryset = Prolog.objects.all()

    @swagger_auto_schema(
        operation_summary='프롤로그2 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    # def get_object(self):
    #     prolog = Prolog.objects.filter(prolog_seq=self.kwargs.get('prolog')).first()
    #     if not prolog:
    #         raise Http404
    #     return prolog

class Cover(generics.CreateAPIView):
    serializer_class = CoverSerializer
    queryset = Cover.objects.all()

    @swagger_auto_schema(
        operation_summary='프롤로그1 API'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    # def get_object(self):
    #     cover = Cover.objects.filter(cover_seq=self.kwargs.get('cover')).first()
    #     if not cover:
    #         raise Http404
    #     return cover

# class DecFront(APIView):
#     def get_object(self, dec_front):#GET,PUT,DELETE
#         try:
#             return DecFront.objects.get(dec_seq=dec_front)
#         except DecFront.DoesNotExist:
#             raise Http404
            
#     def get(self, request, dec_front):
#         decFrontData = self.get_object(dec_front)
#         serializer = DecFrontSerializer(decFrontData)
#         return Response(serializer.data)

#     @swagger_auto_schema( #Nansu POST API 성공.
#         request_body=openapi.Schema(
#             type=openapi.TYPE_OBJECT,
#             properties={
#                 'dec_seq': openapi.Schema(type=openapi.TYPE_INTEGER, description='정수타입', required=['dec_seq'])
#             },#properties에서 ORM하면 됨. 'nansu','nansu_state','permission' 컬럼 추가 가능.
#         ),
#             responses={
#                 400: '에러',
#                 201: '작성된 리소스 정보'
#             },
#             operation_summary='난수 리소스 생성 API',
#             operation_description='난수 리소스를 생성하는 API입니다.'
#         )
#     def post(self, request):
#         serializer = DecFrontSerializer(data=request.data, many=True)
#         print(serializer)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

# class OrderUrlDetail(APIView): #body에 연락처,주소,이름,난수번호 보내야함.
#     def get_object(self, order):
#         try:
#             return Order.objects.get(order_seq=self.kwargs.get('order')).first()
#         except Order.DoesNotExist:
#             raise Http404

#     def get(self, request, order):
#         orderUrl = self.get_object(order)
#         serializer = OrderSerializer(orderUrl)
#         return Response(serializer.data)

#     def post(self, request, order):
#         serializer = OrderSerializer(data=request.data)
#         print(serializer)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ImageView(APIView):
    @swagger_auto_schema( #Nansu POST API 성공.
            operation_summary='Image POST API',
            operation_description='이미지가 sever path에 저장됩니다.'
        )
    def post(self, request, format=None):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderUrlDetail(generics.CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class CalendarUrlDetail(APIView):
    @swagger_auto_schema( #Nansu POST API 성공.
            operation_summary='달력 세부 정보 ex)192.168.0.158:8080/CalendarUrlDetail/1/',
        )
    def get_object(self, calendar):
        try:
            return Calendar.objects.get(calendar_seq=calendar)
        except Calendar.DoesNotExist:
            raise Http404

    def get(self, request, calendar):
        calendarUrl = self.get_object(calendar)
        serializer = CalendarSerializer(calendarUrl)
        return Response(serializer.data)

    def post(self, request, calendar):
        serializer = Serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

