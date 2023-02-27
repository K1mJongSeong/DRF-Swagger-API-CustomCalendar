from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view #api
from rest_framework import status, generics
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Nansu, Order, OrderInfo, Calendar
from .serializers import NansuSerializer, OrderSerializer, OrderInfoSerializer, CalendarSerializer, JanFrontSerializer, JanBackSerializer, FebFrontSerializer, FebBackSerializer, MarFrontSerializer, MarBackSerializer, JuneFrontSerializer, JuneBackSerializer, JulyFrontSerializer, JulyBackSerializer, AugFrontSerializer, AugBackSerializer, SepFrontSerializer, SepBackSerializer, OctFrontSerializer, OctBackSerializer, NovFrontSerializer, NovBackSerializer, DecFrontSerializer, DecBackSerializer, PrologSerializer, CoverSerializer

def index(request):
    return HttpResponse("TEST PAGE")

def nansu(request):
    nansuTest = Nansu.objects.filter(nansu_state='정상')
    print(nansuTest)
    return render(request,'index.html', {"nansuTest":nansuTest})

class HelloWorld(APIView):
    def get(self, request):
        return Response("Hello, World!")

class NansuList(APIView):
    def get(self, request):
        nansuData = Nansu.objects.all()
        serializers = NansuSerializer(nansuData, many=True)
        return Response(serializers.data)

# class OrderList(APIView): #주문 버튼을 누를때 Update
#     def get(self, request):
#         orderData = Order.objects.all()
#         serializers = OrderSerializer(orderData, many=True)
#         return Response(serializers.data)
class OrderList(generics.RetrieveUpdateAPIView): #GET,PUT,PATCH
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    print(queryset)
    loolip_field = '__all__'

class OrderInfoList(APIView):
    def get(self, request):
        nansuInfoData = OrderInfo.objects.all()
        serializers = OrderInfoSerializer(nansuInfoData, many=True)
        return Response(serializers.data)
    def post(self, request, order):
        serializer = Serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

class CalendarList(APIView):
   #@swagger_auto_schema(request_body=CalendarSerializer)
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

class MonthAPI(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                #'month': openapi.Schema(type=openapi.TYPE_STRING, description='월 (예: jan_front, jan_back, ..., dec_back, prolog, cover)'),
                'jan_seq': openapi.Schema(type=openapi.TYPE_INTEGER, description='정수타입',required=['jan_seq']),
                'feb_seq': openapi.Schema(type=openapi.TYPE_INTEGER, description='정수타입',required=['jan_seq']),
            },
        ),
        responses={
            400: '에러',
            201: '작성된 리소스 정보'
        },
        operation_summary='월별 리소스 생성 API',
        operation_description='월별 리소스를 생성하는 API입니다. month 쿼리 매개변수에는 month 값 중 하나를 지정해야 합니다.'
    )
    def post(self, request, month):
        month = request.data.get('month', None)
        #month = kwargs.get('month',None)
        if month is None:
            return Response({'에러'}, status=status.HTTP_400_BAD_REQUEST)
        
        if month == 'jan_front':
            properties={
                'jan_seq': openapi.Schema(type=openapi.TYPE_INTEGER, description='정수타입', required=['jan_seq'])
            }
            serializer = JanFrontSerializer(data=request.data)
            model = JanFront
        elif month == 'jan_back':
            properties={
                'jan_seq': openapi.Schema(type=openapi.TYPE_INTEGER, description='정수타입', required=['jan_seq'])
            }
            serializer = JanBackSerializer(data=request.data)
            model = JanBack
        elif month == 'feb_front':
            properties={
                'feb_seq': openapi.Schema(type=openapi.TYPE_INTEGER, description='정수타입', required=['feb_seq'])
            }
            serializer = FebFrontSerializer(data=request.data)
            model = FebFront
        elif month == 'feb_back':
            properties={
                'feb_seq': openapi.Schema(type=openapi.TYPE_INTEGER, description='정수타입', required=['feb_seq'])
            }
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

class JanFront(APIView):
    def get(self, request):
        janFrontData = JanFront.objects.all()
        serializers = JanFrontSerializer(janFrontData, many=True)
        return Response(serializers.data)
    def post(self, request, jan_front):
        serializer = Serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

class JanBack(APIView):
    def get(self, request):
        janBackData = JanBack.objects.all()
        serializers = JanBackSerializer(janBackData, many=True)
        return Response(serializers.data)
    def post(self, request, jan_back):
        serializer = Serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

class FebFront(APIView):
    def get(self, request):
        febFrontData = FebFront.objects.all()
        serializers = FebFrontSerializer(febFrontData, many=True)
        return Response(serializers.data)
    def post(self, request, feb_front):
        serializer = Serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

class FebBack(APIView):
    def get(self, request):
        febBackData = FebBack.objects.all()
        serializers = FebBackSerializer(febBackData, many=True)
        return Response(serializers.data)
    def post(self, request, feb_back):
        serializer = Serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

class MarFront(APIView):
    def get(self, request):
        marFrontData = MarFront.objects.all()
        serializers = MarFrontSerializer(marFrontData, many=True)
        return Response(serializers.data)
    def post(self, request, order):
        serializer = Serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

class MarBack(APIView):
    def get(self, request):
        marBackData = MarBack.objects.all()
        serializers = MarBackSerializer(marBackData, many=True)
        return Response(serializers.data)
    def post(self, request, order):
        serializer = Serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

class AprilFront(APIView):
    def get(self, request):
        aprilFrontData = AprilFront.objects.all()
        serializers = AprilFrontSerializer(aprilFrontData, many=True)
        return Response(serializers.data)
    def post(self, request, order):
        serializer = Serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

class AprilBack(APIView):
    def get(self, request):
        aprilBackData = AprilBack.objects.all()
        serializers = AprilBackSerializer(aprilBackData, many=True)
        return Response(serializers.data)
    def post(self, request, order):
        serializer = Serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

class MayFront(APIView):
    def get(self, request):
        mayFrontData = MayFront.objects.all()
        serializers = MayFrontSerializer(mayFrontData, many=True)
        return Response(serializers.data)
    def post(self, request, order):
        serializer = Serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

class MayBack(APIView):
    def get(self, request):
        mayBackData = MayBack.objects.all()
        serializers = MayBackSerializer(mayBackData, many=True)
        return Response(serializers.data)
    def post(self, request, order):
        serializer = Serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

class JuneFront(APIView):
    def get(self, request):
        juneFrontData = JuneFront.objects.all()
        serializers = JuneFrontSerializer(juneFrontData, many=True)
        return Response(serializers.data)
    def post(self, request, order):
        serializer = Serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

class JuneBack(APIView):
    def get(self, request):
        juneBackData = JuneBack.objects.all()
        serializers = JuneBackSerializer(juneBackData, many=True)
        return Response(serializers.data)   
    def post(self, request, order):
        serializer = Serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

class JulyFront(APIView):
    def get(self, request):
        julyFrontData = JulyFront.objects.all()
        serializers = JulyFrontSerializer(julyFrontData, many=True)
        return Response(serializers.data)
    def post(self, request, order):
        serializer = Serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JulyBack(APIView):
    def get(self, request):
        julyBackData = JulyBack.objects.all()
        serializers = JulyBackSerializer(julyBackData, many=True)
        return Response(serializers.data)
    def post(self, request, order):
        serializer = Serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AugFront(APIView):
    def get(self, request):
        augFrontData = AugFront.objects.all()
        serializers = AugFrontSerializer(augFrontData, many=True)
        return Response(serializers.data)
    def post(self, request, order):
        serializer = Serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AugBack(APIView):
    def get(self, request):
        augBackData = AugBack.objects.all()
        serializers = AugBackSerializer(augBackData, many=True)
        return Response(serializers.data)
    def post(self, request, order):
        serializer = Serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SepFront(APIView):
    def get(self, request):
        sepFrontData = SepFront.objects.all()
        serializers = SepFrontSerializer(sepFrontData, many=True)
        return Response(serializers.data)
    def post(self, request, order):
        serializer = Serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SepBack(APIView):
    def get(self, request):
        sepBackData = SepBack.objects.all()
        serializers = SepBackSerializer(sepBackData, many=True)
        return Response(serializers.data)
    def post(self, request, order):
        serializer = Serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OctFront(APIView):
    def get(self, request):
        octFrontData = OctFront.objects.all()
        serializers = OctFrontSerializer(octFrontData, many=True)
        return Response(serializers.data)
    def post(self, request, order):
        serializer = Serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OctBack(APIView):
    def get(self, request):
        octBackData = OctBack.objects.all()
        serializers = OctBackSerializer(octBackData, many=True)
        return Response(serializers.data) 
    def post(self, request, order):
        serializer = Serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NovFront(APIView):
    def get(self, request):
        novFrontData = NovFront.objects.all()
        serializers = NovFrontSerializer(novFrontData, many=True)
        return Response(serializers.data)
    def post(self, request, order):
        serializer = Serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NovBack(APIView):
    def get(self, request):
        novBackData = NovBack.objects.all()
        serializers = NovBackSerializer(novBackData, many=True)
        return Response(serializers.data)
    def post(self, request, order):
        serializer = Serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DecFront(APIView):
    def get(self, request):
        decFrontData = DecFront.objects.all()
        serializers = DecFrontSerializer(decFrontData, many=True)
        return Response(serializers.data)
    def post(self, request, order):
        serializer = Serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DecBack(APIView):
    def get(self, request):
        decBackData = DecBack.objects.all()
        serializers = DecBackSerializer(decBackData, many=True)
        return Response(serializers.data) 
    def post(self, request, order):
        serializer = Serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Prolog(APIView):
    def get(self, request):
        prologData = Prolog.objects.all()
        serializers = PrologSerializer(prologData, many=True)
        return Response(serializers.data)
    def post(self, request, order):
        serializer = Serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
class Cover(APIView):
    def get(self, request):
        coverData = Cover.objects.all()
        serializers = CoverSerializer(coverData, many=True)
        return Response(serializers.data) 
    def post(self, request, order):
        serializer = Serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#@csrf_exempt
class NansuUrlDetail(APIView):
    def get_object(self, nansu):#GET,PUT,DELETE
        try:
            return Nansu.objects.get(nansu_seq=nansu)
        except Nansu.DoesNotExist:
            raise Http404

    def get(self, request, nansu):
        nansuUrl = self.get_object(nansu)
        serializer = NansuSerializer(nansuUrl)
        return Response(serializer.data)

    def put(self, request, nansu): 
        nansuUrl = self.get_object(nansu)
        serializer = NansuSerializer(nansuUrl, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

    def delete(self, request, nansu):
        nansuUrl = self.get_object(nansu)
        nansuUrl.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderUrlDetail(APIView):
    def get_object(self, order):
        try:
            return Order.objects.get(order_seq=order)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, order):
        orderUrl = self.get_object(order)
        serializer = OrderSerializer(orderUrl)
        return Response(serializer.data)

    def post(self, request, order):
        serializer = Serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, order):
        orderUrl = self.get_object(order)
        orderUrl.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CalendarUrlDetail(APIView):
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

