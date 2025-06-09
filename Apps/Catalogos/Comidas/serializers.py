from rest_framework.serializers import ModelSerializer, CharField
from rest_framework.views import APIView

from .models import foods

class ComidasSerializer(ModelSerializer):
    tipocomida = CharField(source='typeFoodFK.description_typefood', read_only=True, label='Tipo de comida')

    class Meta:
        model = foods
        fields = ['idFood', 'foodName', 'foodDescription', 'Ingredients_food', 'typeFoodFK', 'tipocomida']