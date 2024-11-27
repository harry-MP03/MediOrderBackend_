from rest_framework.serializers import ModelSerializer, CharField

from .models import typeBeverage

class typeBeverageSerializer(ModelSerializer):
    class Meta:
        model = typeBeverage
        fields = ['description_TypeBeverage']