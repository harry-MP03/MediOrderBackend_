from rest_framework.serializers import ModelSerializer, CharField

from .models import beverages, typeBeverage

class BeverageSerializer(ModelSerializer):
    tipoBebidaNombre = CharField(source='typeBeverage.description_TypeBeverage', read_only=True)
    class Meta:
        model = beverages
        fields = ['NameBeverage', 'Beverage_description', 'Ingredients_Beverage','typeBeveragesFK', 'tipoBebidaNombre']