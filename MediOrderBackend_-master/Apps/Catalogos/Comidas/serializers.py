from rest_framework.serializers import ModelSerializer, CharField

from .models import foods

class FoodSerializer(ModelSerializer):
    class Meta:
        model = foods
        fields = ['foodName', 'foodDescription', 'Ingredients_food', 'typeFoodFK']

#Para los reportes de pedidos
class ComidaSoporteSerializer(ModelSerializer):
    tipoComida = CharField(source='typeFoodFK.description_typefood', read_only=True, label='Tipo de Comida')
    class Meta:
        model = foods
        fields = ['tipoComida', 'foodName']