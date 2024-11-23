from rest_framework.serializers import ModelSerializer

from .models import beverages

class BeverageSerializer(ModelSerializer):
    class Meta:
        model = beverages
        fields = ['NameBeverage', 'Beverage_description', 'Ingredients_Beverage', 'typeBeveragesFK']