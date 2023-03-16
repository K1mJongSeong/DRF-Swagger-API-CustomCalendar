from rest_framework import serializers
from rest_framework.parsers import MultiPartParser
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from .models import Nansu, Order, OrderInfo, Calendar, JanFront, JanBack, FebFront, FebBack, MarFront, MarBack, AprilFront, AprilBack, MayFront, MayBack, JuneFront, JuneBack, JulyFront, JulyBack, AugFront, AugBack, SepFront, SepBack, OctFront, OctBack, NovFront, NovBack, DecFront, DecBack, Prolog, Cover, Image, Notice

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'

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
        fields = ('user_name','user_phone','address','nansu','postcode','detailAddress','orderState')

class OrderInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderInfo
        fields = '__all__'

class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = '__all__'         


class JanFrontSerializer(serializers.ModelSerializer):
    jan_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = JanFront
        fields = '__all__'

class JanBackSerializer(serializers.ModelSerializer):
    jan_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = JanBack
        fields = '__all__'



class FebFrontSerializer(serializers.ModelSerializer):
    feb_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = FebFront
        fields = '__all__'

class FebBackSerializer(serializers.ModelSerializer):
    feb_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = FebBack
        fields = '__all__'




class MarFrontSerializer(serializers.ModelSerializer):
    mar_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = MarFront
        fields = '__all__'

class MarBackSerializer(serializers.ModelSerializer):
    mar_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = MarBack
        fields = '__all__'



class AprilFrontSerializer(serializers.ModelSerializer):
    april_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = AprilFront
        fields = '__all__'

class AprilBackSerializer(serializers.ModelSerializer):
    april_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = AprilBack
        fields = '__all__'



class MayFrontSerializer(serializers.ModelSerializer):
    may_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = MayFront
        fields = '__all__'

class MayBackSerializer(serializers.ModelSerializer):
    may_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = MayBack
        fields = '__all__'



class JuneFrontSerializer(serializers.ModelSerializer):
    june_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = JuneFront
        fields = '__all__'

class JuneBackSerializer(serializers.ModelSerializer):
    june_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = JuneBack
        fields = '__all__'



class JulyFrontSerializer(serializers.ModelSerializer):
    july_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = JulyFront
        fields = '__all__'

class JulyBackSerializer(serializers.ModelSerializer):
    july_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = JulyBack
        fields = '__all__'



class AugFrontSerializer(serializers.ModelSerializer):
    aug_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = AugFront
        fields = '__all__'

class AugBackSerializer(serializers.ModelSerializer):
    aug_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = AugBack
        fields = '__all__'



class SepFrontSerializer(serializers.ModelSerializer):
    sep_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = SepFront
        fields = '__all__'

class SepBackSerializer(serializers.ModelSerializer):
    sep_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = SepBack
        fields = '__all__'



class OctFrontSerializer(serializers.ModelSerializer):
    oct_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = OctFront
        fields = '__all__'

class OctBackSerializer(serializers.ModelSerializer):
    oct_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = OctBack
        fields = '__all__'



class NovFrontSerializer(serializers.ModelSerializer):
    nov_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = NovFront
        fields = '__all__'

class NovBackSerializer(serializers.ModelSerializer):
    nov_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = NovBack
        fields = '__all__'



class DecFrontSerializer(serializers.ModelSerializer):
    dec_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = DecFront
        fields = '__all__'

class DecBackSerializer(serializers.ModelSerializer):
    dec_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = DecBack
        fields = '__all__'



class PrologSerializer(serializers.ModelSerializer):
    prolog_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = Prolog
        fields = '__all__'



class CoverSerializer(serializers.ModelSerializer):
    cover_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = Cover
        fields = '__all__'