from rest_framework import serializers
from rest_framework.parsers import MultiPartParser
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.serializers.json import DjangoJSONEncoder
from io import BytesIO
from .models import Nansu, Order, OrderInfo, Calendar, JanFront, JanBack, FebFront, FebBack, MarFront, MarBack, AprilFront, AprilBack, MayFront, MayBack, JuneFront, JuneBack, JulyFront, JulyBack, AugFront, AugBack, SepFront, SepBack, OctFront, OctBack, NovFront, NovBack, DecFront, DecBack, Prolog, Cover, Image, Notice, NansuInfo

class NansuInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NansuInfo
        fields = '__all__'

class NoticeSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")

    class Meta:
        model = Notice
        fields = ('notice','monthdays','nansu')

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class NansuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nansu
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('user_name','user_phone','address','nansu','postcode','detailAddress','orderState','order_date')

class OrderInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderInfo
        fields = '__all__'

class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = '__all__'         


class JanFrontSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = JanFront
        fields = ('pic','nansu','memo')

class JanBackSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = JanBack
        fields = ('pic','nansu')



class FebFrontSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = FebFront
        fields = ('pic','nansu','memo')

class FebBackSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = FebBack
        fields = ('pic','nansu')




class MarFrontSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = MarFront
        fields = ('pic','nansu','memo')

class MarBackSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = MarBack
        fields = ('pic','nansu')



class AprilFrontSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = AprilFront
        fields = ('pic','nansu','memo')

class AprilBackSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = AprilBack
        fields = ('pic','nansu')



class MayFrontSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = MayFront
        fields = ('pic','nansu','memo')

class MayBackSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = MayBack
        fields = ('pic','nansu')



class JuneFrontSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = JuneFront
        fields = ('pic','nansu','memo')

class JuneBackSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = JuneBack
        fields = ('pic','nansu')



class JulyFrontSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = JulyFront
        fields = ('pic','nansu','memo')

class JulyBackSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = JulyBack
        fields = ('pic','nansu')



class AugFrontSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = AugFront
        fields = ('pic','nansu','memo')

class AugBackSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = AugBack
        fields = ('pic','nansu')



class SepFrontSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = SepFront
        fields = ('pic','nansu','memo')

class SepBackSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = SepBack
        fields = ('pic','nansu')



class OctFrontSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = OctFront
        fields = ('pic','nansu','memo')

class OctBackSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = OctBack
        fields = ('pic','nansu')



class NovFrontSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = NovFront
        fields = ('pic','nansu','memo')

class NovBackSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = NovBack
        fields = ('pic','nansu')



class DecFrontSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = DecFront
        fields = ('pic','nansu','memo')

class DecBackSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = DecBack
        fields = ('pic','nansu')



class PrologSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = Prolog
        fields = ('pic','nansu')



class CoverSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = Cover
        fields = ('pic','nansu')