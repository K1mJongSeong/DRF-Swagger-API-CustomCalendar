from rest_framework import serializers
from .models import Nansu, Order, OrderInfo, Calendar, JanFront, JanBack, FebFront, FebBack, MarFront, MarBack, AprilFront, AprilBack, MayFront, MayBack, JuneFront, JuneBack, JulyFront, JulyBack, AugFront, AugBack, SepFront, SepBack, OctFront, OctBack, NovFront, NovBack, DecFront, DecBack, Prolog, Cover

class NansuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nansu
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderInfo
        fields = '__all__'

class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = '__all__'                



class JanFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = JanFront
        field = '__all__'

class JanBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = JanBack
        field = '__all__'



class FebFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = FebFront
        field = '__all__'

class FebBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FebBack
        field = '__all__'



class MarFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarFront
        field = '__all__'

class MarBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarBack
        field = '__all__'



class AprilFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = AprilFront
        field = '__all__'

class AprilBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = AprilBack
        field = '__all__'



class MayFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = MayFront
        field = '__all__'

class MayBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = MayBack
        field = '__all__'



class JuneFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = JuneFront
        field = '__all__'

class JuneBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = JuneBack
        field = '__all__'



class JulyFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = JulyFront
        field = '__all__'

class JulyBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = JulyBack
        field = '__all__'



class AugFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = AugFront
        field = '__all__'

class AugBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = AugBack
        field = '__all__'



class SepFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = SepFront
        field = '__all__'

class SepBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = SepBack
        field = '__all__'



class OctFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = OctFront
        field = '__all__'

class OctBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = OctBack
        field = '__all__'



class NovFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = NovFront
        field = '__all__'

class NovBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = NovBack
        field = '__all__'



class DecFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = DecFront
        field = '__all__'

class DecBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = DecBack
        field = '__all__'



class PrologSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prolog
        field = '__all__'



class CoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cover
        field = '__all__'