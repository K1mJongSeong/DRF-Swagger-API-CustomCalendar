from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view #api
from rest_framework import generics
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
    def get(self, request):
        calendarData = Calendar.objects.all()
        serializers = CalendarSerializer(calendarData, many=True)
        return Response(serializers.data)
    def post(self, request, order):
        serializer = Serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

class JanFront(APIView):
    def get(self, request):
        janFrontData = JanFront.objects.all()
        serializers = JanFrontSerializer(janFrontData, many=True)
        return Response(serializers.data)
    def post(self, request, order):
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
    def post(self, request, order):
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
    def post(self, request, order):
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
    def post(self, request, order):
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


class NansuUrlDetail(APIView): #url에 NansuUrlDetail/1 입력하면 nansu_seq=1 데이터나옴(테스트용)
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

