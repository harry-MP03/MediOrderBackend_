from rest_framework.serializers import ModelSerializer, CharField

from .models import beverages, typeBeverage

class BebidasConTiposSerializer(ModelSerializer):
    class Meta:
        model = typeBeverage
        fields = ['description_TypeBeverage']

class BeverageSerializer(ModelSerializer):
    nombreTipoBebida = CharField(source='typeBeveragesFK.description_TypeBeverage', read_only=True, label= 'Nombre de Tipo de bebida')


    class Meta:
        model = beverages
        fields = ['NameBeverage', 'Beverage_description', 'Ingredients_Beverage','typeBeveragesFK' ,'nombreTipoBebida']

