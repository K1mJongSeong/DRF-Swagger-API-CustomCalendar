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
    jan_nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    jan_pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = JanFront
        fields = ('jan_pic','jan_nansu','jan_memo')

class JanBackSerializer(serializers.ModelSerializer):
    jan_nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    jan_pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = JanBack
        fields = ('jan_pic','jan_nansu')



class FebFrontSerializer(serializers.ModelSerializer):
    feb_nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    feb_pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = FebFront
        fields = ('feb_pic','feb_nansu','feb_memo')

class FebBackSerializer(serializers.ModelSerializer):
    feb_nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    feb_pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = FebBack
        fields = ('feb_pic','feb_nansu')




class MarFrontSerializer(serializers.ModelSerializer):
    mar_nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    mar_pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = MarFront
        fields = ('mar_pic','mar_nansu','mar_memo')

class MarBackSerializer(serializers.ModelSerializer):
    mar_nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    mar_pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = MarBack
        fields = ('mar_pic','mar_nansu')



class AprilFrontSerializer(serializers.ModelSerializer):
    april_nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    april_pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = AprilFront
        fields = ('april_pic','april_nansu','april_memo')

class AprilBackSerializer(serializers.ModelSerializer):
    april_nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    april_pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = AprilBack
        fields = ('april_pic','april_nansu')



class MayFrontSerializer(serializers.ModelSerializer):
    may_nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    may_pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = MayFront
        fields = ('may_pic','may_nansu','may_memo')

class MayBackSerializer(serializers.ModelSerializer):
    may_nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    may_pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = MayBack
        fields = ('may_pic','may_nansu')



class JuneFrontSerializer(serializers.ModelSerializer):
    june_nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    june_pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = JuneFront
        fields = ('june_pic','june_nansu','june_memo')

class JuneBackSerializer(serializers.ModelSerializer):
    june_nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    june_pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = JuneBack
        fields = ('june_pic','june_nansu')



class JulyFrontSerializer(serializers.ModelSerializer):
    july_nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    july_pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = JulyFront
        fields = ('july_pic','july_nansu','july_memo')

class JulyBackSerializer(serializers.ModelSerializer):
    july_nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    july_pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = JulyBack
        fields = ('july_pic','july_nansu')



class AugFrontSerializer(serializers.ModelSerializer):
    aug_nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    aug_pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = AugFront
        fields = ('aug_pic','aug_nansu','aug_memo')

class AugBackSerializer(serializers.ModelSerializer):
    aug_nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    aug_pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = AugBack
        fields = ('aug_pic','aug_nansu')



class SepFrontSerializer(serializers.ModelSerializer):
    sep_nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    sep_pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = SepFront
        fields = ('sep_pic','sep_nansu','sep_memo')

class SepBackSerializer(serializers.ModelSerializer):
    sep_nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    sep_pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = SepBack
        fields = ('sep_pic','sep_nansu')



class OctFrontSerializer(serializers.ModelSerializer):
    oct_nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    oct_pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = OctFront
        fields = ('oct_pic','oct_nansu','oct_memo')

class OctBackSerializer(serializers.ModelSerializer):
    oct_nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    oct_pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = OctBack
        fields = ('oct_pic','oct_nansu')



class NovFrontSerializer(serializers.ModelSerializer):
    nov_nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    nov_pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = NovFront
        fields = ('nov_pic','nov_nansu','nov_memo')

class NovBackSerializer(serializers.ModelSerializer):
    nov_nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    nov_pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = NovBack
        fields = ('nov_pic','nov_nansu')



class DecFrontSerializer(serializers.ModelSerializer):
    dec_nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    dec_pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = DecFront
        fields = ('dec_pic','dec_nansu','dec_memo')

class DecBackSerializer(serializers.ModelSerializer):
    dec_nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    dec_pic = serializers.JSONField(encoder=DjangoJSONEncoder, required=False)
    class Meta:
        model = DecBack
        fields = ('dec_pic','dec_nansu')



class PrologSerializer(serializers.ModelSerializer):
    prolog_nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    prolog_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = Prolog
        fields = ('prolog_pic','prolog_nansu')



class CoverSerializer(serializers.ModelSerializer):
    cover_nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    cover_pic = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    class Meta:
        model = Cover
        fields = ('cover_pic','cover_nansu')