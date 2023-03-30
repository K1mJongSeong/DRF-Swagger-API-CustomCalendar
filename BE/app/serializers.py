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
    # def validate_nansu(self, value):
    #     # nansu 값이 유효한지 여부를 검증하는 로직을 작성합니다.
    #     if len(value) != 7:
    #         raise serializers.ValidationError('nansu는 6자리 문자열이어야 합니다.')
    #     return value

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
        fields = ('user_name','user_phone','address','nansu','postcode','detailAddress','orderState','order_date','pic')

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
    pic = serializers.CharField(required=False, allow_blank=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['pic']:
            data['pic'] = [url.strip() for url in data['pic'].strip('][').split(',')]
        return data

    def to_internal_value(self, data):
        if 'pic' in data:
            data['pic'] = str(data['pic'])  # 리스트를 문자열로 변환
        return super().to_internal_value(data)

    class Meta:
        model = JanFront
        fields = ('pic','nansu','total_pic')


class JanBackSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.CharField(required=False, allow_blank=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['pic']:
            data['pic'] = [url.strip() for url in data['pic'].strip('][').split(',')]
        return data

    def to_internal_value(self, data):
        if 'pic' in data:
            data['pic'] = str(data['pic'])  # 리스트를 문자열로 변환
        return super().to_internal_value(data)

    class Meta:
        model = JanBack
        fields = ('pic','nansu','total_pic')




class FebFrontSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.CharField(required=False, allow_blank=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['pic']:
            data['pic'] = [url.strip() for url in data['pic'].strip('][').split(',')]
        return data

    def to_internal_value(self, data):
        if 'pic' in data:
            data['pic'] = str(data['pic'])  # 리스트를 문자열로 변환
        return super().to_internal_value(data)

    class Meta:
        model = FebFront
        fields = ('pic','nansu','total_pic')

class FebBackSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.CharField(required=False, allow_blank=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['pic']:
            data['pic'] = [url.strip() for url in data['pic'].strip('][').split(',')]
        return data

    def to_internal_value(self, data):
        if 'pic' in data:
            data['pic'] = str(data['pic'])  # 리스트를 문자열로 변환
        return super().to_internal_value(data)

    class Meta:
        model = FebBack
        fields = ('pic','nansu','total_pic')




class MarFrontSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.CharField(required=False, allow_blank=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['pic']:
            data['pic'] = [url.strip() for url in data['pic'].strip('][').split(',')]
        return data

    def to_internal_value(self, data):
        if 'pic' in data:
            data['pic'] = str(data['pic'])  # 리스트를 문자열로 변환
        return super().to_internal_value(data)

    class Meta:
        model = MarFront
        fields = ('pic','nansu','total_pic')

class MarBackSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.CharField(required=False, allow_blank=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['pic']:
            data['pic'] = [url.strip() for url in data['pic'].strip('][').split(',')]
        return data

    def to_internal_value(self, data):
        if 'pic' in data:
            data['pic'] = str(data['pic'])  # 리스트를 문자열로 변환
        return super().to_internal_value(data)

    class Meta:
        model = MarBack
        fields = ('pic','nansu','total_pic')



class AprilFrontSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.CharField(required=False, allow_blank=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['pic']:
            data['pic'] = [url.strip() for url in data['pic'].strip('][').split(',')]
        return data

    def to_internal_value(self, data):
        if 'pic' in data:
            data['pic'] = str(data['pic'])  # 리스트를 문자열로 변환
        return super().to_internal_value(data)

    class Meta:
        model = AprilFront
        fields = ('pic','nansu','total_pic')

class AprilBackSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.CharField(required=False, allow_blank=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['pic']:
            data['pic'] = [url.strip() for url in data['pic'].strip('][').split(',')]
        return data

    def to_internal_value(self, data):
        if 'pic' in data:
            data['pic'] = str(data['pic'])  # 리스트를 문자열로 변환
        return super().to_internal_value(data)

    class Meta:
        model = AprilBack
        fields = ('pic','nansu','total_pic')



class MayFrontSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.CharField(required=False, allow_blank=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['pic']:
            data['pic'] = [url.strip() for url in data['pic'].strip('][').split(',')]
        return data

    def to_internal_value(self, data):
        if 'pic' in data:
            data['pic'] = str(data['pic'])  # 리스트를 문자열로 변환
        return super().to_internal_value(data)

    class Meta:
        model = MayFront
        fields = ('pic','nansu','total_pic')

class MayBackSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.CharField(required=False, allow_blank=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['pic']:
            data['pic'] = [url.strip() for url in data['pic'].strip('][').split(',')]
        return data

    def to_internal_value(self, data):
        if 'pic' in data:
            data['pic'] = str(data['pic'])  # 리스트를 문자열로 변환
        return super().to_internal_value(data)

    class Meta:
        model = MayBack
        fields = ('pic','nansu','total_pic')



class JuneFrontSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.CharField(required=False, allow_blank=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['pic']:
            data['pic'] = [url.strip() for url in data['pic'].strip('][').split(',')]
        return data

    def to_internal_value(self, data):
        if 'pic' in data:
            data['pic'] = str(data['pic'])  # 리스트를 문자열로 변환
        return super().to_internal_value(data)

    class Meta:
        model = JuneFront
        fields = ('pic','nansu','total_pic')

class JuneBackSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.CharField(required=False, allow_blank=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['pic']:
            data['pic'] = [url.strip() for url in data['pic'].strip('][').split(',')]
        return data

    def to_internal_value(self, data):
        if 'pic' in data:
            data['pic'] = str(data['pic'])  # 리스트를 문자열로 변환
        return super().to_internal_value(data)

    class Meta:
        model = JuneBack
        fields = ('pic','nansu','total_pic')



class JulyFrontSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.CharField(required=False, allow_blank=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['pic']:
            data['pic'] = [url.strip() for url in data['pic'].strip('][').split(',')]
        return data

    def to_internal_value(self, data):
        if 'pic' in data:
            data['pic'] = str(data['pic'])  # 리스트를 문자열로 변환
        return super().to_internal_value(data)

    class Meta:
        model = JulyFront
        fields = ('pic','nansu','total_pic')

class JulyBackSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.CharField(required=False, allow_blank=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['pic']:
            data['pic'] = [url.strip() for url in data['pic'].strip('][').split(',')]
        return data

    def to_internal_value(self, data):
        if 'pic' in data:
            data['pic'] = str(data['pic'])  # 리스트를 문자열로 변환
        return super().to_internal_value(data)

    class Meta:
        model = JulyBack
        fields = ('pic','nansu','total_pic')



class AugFrontSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.CharField(required=False, allow_blank=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['pic']:
            data['pic'] = [url.strip() for url in data['pic'].strip('][').split(',')]
        return data

    def to_internal_value(self, data):
        if 'pic' in data:
            data['pic'] = str(data['pic'])  # 리스트를 문자열로 변환
        return super().to_internal_value(data)

    class Meta:
        model = AugFront
        fields = ('pic','nansu','total_pic')

class AugBackSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.CharField(required=False, allow_blank=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['pic']:
            data['pic'] = [url.strip() for url in data['pic'].strip('][').split(',')]
        return data

    def to_internal_value(self, data):
        if 'pic' in data:
            data['pic'] = str(data['pic'])  # 리스트를 문자열로 변환
        return super().to_internal_value(data)

    class Meta:
        model = AugBack
        fields = ('pic','nansu','total_pic')



class SepFrontSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.CharField(required=False, allow_blank=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['pic']:
            data['pic'] = [url.strip() for url in data['pic'].strip('][').split(',')]
        return data

    def to_internal_value(self, data):
        if 'pic' in data:
            data['pic'] = str(data['pic'])  # 리스트를 문자열로 변환
        return super().to_internal_value(data)

    class Meta:
        model = SepFront
        fields = ('pic','nansu','total_pic')

class SepBackSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.CharField(required=False, allow_blank=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['pic']:
            data['pic'] = [url.strip() for url in data['pic'].strip('][').split(',')]
        return data

    def to_internal_value(self, data):
        if 'pic' in data:
            data['pic'] = str(data['pic'])  # 리스트를 문자열로 변환
        return super().to_internal_value(data)

    class Meta:
        model = SepBack
        fields = ('pic','nansu','total_pic')



class OctFrontSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.CharField(required=False, allow_blank=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['pic']:
            data['pic'] = [url.strip() for url in data['pic'].strip('][').split(',')]
        return data

    def to_internal_value(self, data):
        if 'pic' in data:
            data['pic'] = str(data['pic'])  # 리스트를 문자열로 변환
        return super().to_internal_value(data)

    class Meta:
        model = OctFront
        fields = ('pic','nansu','total_pic')

class OctBackSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.CharField(required=False, allow_blank=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['pic']:
            data['pic'] = [url.strip() for url in data['pic'].strip('][').split(',')]
        return data

    def to_internal_value(self, data):
        if 'pic' in data:
            data['pic'] = str(data['pic'])  # 리스트를 문자열로 변환
        return super().to_internal_value(data)

    class Meta:
        model = OctBack
        fields = ('pic','nansu','total_pic')



class NovFrontSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.CharField(required=False, allow_blank=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['pic']:
            data['pic'] = [url.strip() for url in data['pic'].strip('][').split(',')]
        return data

    def to_internal_value(self, data):
        if 'pic' in data:
            data['pic'] = str(data['pic'])  # 리스트를 문자열로 변환
        return super().to_internal_value(data)

    class Meta:
        model = NovFront
        fields = ('pic','nansu','total_pic')

class NovBackSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.CharField(required=False, allow_blank=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['pic']:
            data['pic'] = [url.strip() for url in data['pic'].strip('][').split(',')]
        return data

    def to_internal_value(self, data):
        if 'pic' in data:
            data['pic'] = str(data['pic'])  # 리스트를 문자열로 변환
        return super().to_internal_value(data)

    class Meta:
        model = NovBack
        fields = ('pic','nansu','total_pic')



class DecFrontSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.CharField(required=False, allow_blank=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['pic']:
            data['pic'] = [url.strip() for url in data['pic'].strip('][').split(',')]
        return data

    def to_internal_value(self, data):
        if 'pic' in data:
            data['pic'] = str(data['pic'])  # 리스트를 문자열로 변환
        return super().to_internal_value(data)

    class Meta:
        model = DecFront
        fields = ('pic','nansu','total_pic')

class DecBackSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.CharField(required=False, allow_blank=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['pic']:
            data['pic'] = [url.strip() for url in data['pic'].strip('][').split(',')]
        return data

    def to_internal_value(self, data):
        if 'pic' in data:
            data['pic'] = str(data['pic'])  # 리스트를 문자열로 변환
        return super().to_internal_value(data)

    class Meta:
        model = DecBack
        fields = ('pic','nansu','total_pic')



class PrologSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.CharField(required=False, allow_blank=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['pic']:
            data['pic'] = [url.strip() for url in data['pic'].strip('][').split(',')]
        return data

    def to_internal_value(self, data):
        if 'pic' in data:
            data['pic'] = str(data['pic'])  # 리스트를 문자열로 변환
        return super().to_internal_value(data)

    class Meta:
        model = Prolog
        fields = ('pic','nansu','total_pic')



class CoverSerializer(serializers.ModelSerializer):
    nansu = serializers.CharField(required=True, help_text="nansu 필수 입력")
    pic = serializers.CharField(required=False, allow_blank=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['pic']:
            data['pic'] = [url.strip() for url in data['pic'].strip('][').split(',')]
        return data

    def to_internal_value(self, data):
        if 'pic' in data:
            data['pic'] = str(data['pic'])  # 리스트를 문자열로 변환
        return super().to_internal_value(data)

    class Meta:
        model = Cover
        fields = ('pic','nansu','total_pic')