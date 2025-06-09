from rest_framework.serializers import ModelSerializer

from .models import typeBeverage

class TypeBeverageSerializer(ModelSerializer):
    class Meta:
        model = typeBeverage
        fields = ['id_typeBeverage', 'description_TypeBeverage']
