from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Nansu,Order, OrderInfo, Calendar
from .serializers import NansuSerializer, OrderSerializer, OrderInfoSerializer, CalendarSerializer

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
class OrderList(generics.RetrieveUpdateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    print(queryset)
    loolip_field = 'order_seq'

class OrderInfoList(APIView):
    def get(self, request):
        nansuInfoData = OrderInfo.objects.all()
        serializers = OrderInfoSerializer(nansuInfoData, many=True)
        return Response(serializers.data)

class CalendarList(APIView):
    def get(self, request):
        calendarData = Calendar.objects.all()
        serializers = CalendarSerializer(calendarData, many=True)
        return Response(serializers.data)

class NansuUrlDetail(APIView): #url에 NansuUrlDetail/1 입력하면 nansu_seq=1 데이터나옴(테스트용)
    def get_object(self, nansu):
        try:
            return Nansu.objects.get(nansu_seq=1)
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