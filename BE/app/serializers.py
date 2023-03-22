from rest_framework import serializers
from rest_framework.parsers import MultiPartParser
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from .models import Nansu, Order, OrderInfo, Calendar, JanFront, JanBack, FebFront, FebBack, MarFront, MarBack, AprilFront, AprilBack, MayFront, MayBack, JuneFront, JuneBack, JulyFront, JulyBack, AugFront, AugBack, SepFront, SepBack, OctFront, OctBack, NovFront, NovBack, DecFront, DecBack, Prolog, Cover, Image, Notice

class NoticeSerializer(serializers.ModelSerializer):
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
    jan_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = JanFront
        fields = ('jan_pic','jan_nansu','jan_memo')

class JanBackSerializer(serializers.ModelSerializer):
    jan_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = JanBack
        fields = ('jan_pic','jan_nansu')



class FebFrontSerializer(serializers.ModelSerializer):
    feb_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = FebFront
        fields = ('feb_pic','feb_nansu','feb_memo')

class FebBackSerializer(serializers.ModelSerializer):
    feb_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = FebBack
        fields = ('feb_pic','feb_nansu')




class MarFrontSerializer(serializers.ModelSerializer):
    mar_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = MarFront
        fields = ('mar_pic','mar_nansu','mar_memo')

class MarBackSerializer(serializers.ModelSerializer):
    mar_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = MarBack
        fields = ('mar_pic','mar_nansu')



class AprilFrontSerializer(serializers.ModelSerializer):
    april_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = AprilFront
        fields = ('april_pic','april_nansu','april_memo')

class AprilBackSerializer(serializers.ModelSerializer):
    april_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = AprilBack
        fields = ('april_pic','april_nansu')



class MayFrontSerializer(serializers.ModelSerializer):
    may_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = MayFront
        fields = ('may_pic','may_nansu','may_memo')

class MayBackSerializer(serializers.ModelSerializer):
    may_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = MayBack
        fields = ('may_pic','may_nansu')



class JuneFrontSerializer(serializers.ModelSerializer):
    june_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = JuneFront
        fields = ('june_pic','june_nansu','june_memo')

class JuneBackSerializer(serializers.ModelSerializer):
    june_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = JuneBack
        fields = ('june_pic','june_nansu')



class JulyFrontSerializer(serializers.ModelSerializer):
    july_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = JulyFront
        fields = ('july_pic','july_nansu','july_memo')

class JulyBackSerializer(serializers.ModelSerializer):
    july_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = JulyBack
        fields = ('july_pic','july_nansu')



class AugFrontSerializer(serializers.ModelSerializer):
    aug_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = AugFront
        fields = ('aug_pic','aug_nansu','aug_memo')

class AugBackSerializer(serializers.ModelSerializer):
    aug_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = AugBack
        fields = ('aug_pic','aug_nansu')



class SepFrontSerializer(serializers.ModelSerializer):
    sep_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = SepFront
        fields = ('sep_pic','sep_nansu','sep_memo')

class SepBackSerializer(serializers.ModelSerializer):
    sep_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = SepBack
        fields = ('sep_pic','sep_nansu')



class OctFrontSerializer(serializers.ModelSerializer):
    oct_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = OctFront
        fields = ('oct_pic','oct_nansu','oct_memo')

class OctBackSerializer(serializers.ModelSerializer):
    oct_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = OctBack
        fields = ('oct_pic','oct_nansu')



class NovFrontSerializer(serializers.ModelSerializer):
    nov_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = NovFront
        fields = ('nov_pic','nov_nansu','nov_memo')

class NovBackSerializer(serializers.ModelSerializer):
    nov_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = NovBack
        fields = ('nov_pic','nov_nansu')



class DecFrontSerializer(serializers.ModelSerializer):
    dec_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = DecFront
        fields = ('dec_pic','dec_nansu','dec_memo')

class DecBackSerializer(serializers.ModelSerializer):
    dec_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = DecBack
        fields = ('dec_pic','dec_nansu')



class PrologSerializer(serializers.ModelSerializer):
    prolog_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = Prolog
        fields = ('prolog_pic','prolog_nansu')



class CoverSerializer(serializers.ModelSerializer):
    cover_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = Cover
        fields = ('cover_pic','cover_nansu')