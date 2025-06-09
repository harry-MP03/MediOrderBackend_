from rest_framework.serializers import ModelSerializer, CharField

from .models import beverages, typeBeverage

class BeverageSerializer(ModelSerializer):
    nombreTipoBebida = CharField(source='typeBeveragesFK.description_TypeBeverage', read_only=True, label= 'Nombre de Tipo de bebida')


    class Meta:
        model = beverages
        fields = ['idBeverages', 'NameBeverage', 'Beverage_description', 'Ingredients_Beverage','typeBeveragesFK' ,'nombreTipoBebida']

