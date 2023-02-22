from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Nansu
from .serializers import NansuSerializer

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

class NansuUrlDetail(APIView):
    def get_object(self, nansu):
        try:
            return Nansu.objects.get(nansu_seq=1)
        except Nansu.DoesNotExist:
            raise Http404

    def get(self, request, nansu):
        book = self.get_object(nansu)
        serializer = NansuSerializer(book)
        return Response(serializer.data)

    def put(self, request, nansu):
        book = self.get_object(nansu)
        serializer = NansuSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, nansu):
        book = self.get_object(nansu)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)