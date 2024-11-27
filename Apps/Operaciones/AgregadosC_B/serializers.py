from rest_framework.serializers import ModelSerializer, CharField

from Apps.Catalogos.Bebidas.models import beverages
from Apps.Catalogos.TiposBebida.models import typeBeverage

class Bebidas_Serializer(ModelSerializer):
    nombreTiposBebidas = CharField(source='beverages.NameBeverage',read_only=True)
    DescripcionBebidas = CharField(source='beverages.DescriptionBeverage',read_only=True)
    IngredientesBebidas = CharField(source='beverages.IngredienteBeverage',read_only=True)
    model = beverages
    fields = ['']

    class Meta:
        model = typeBeverage
        fields = ['description_TypeBeverage']

class Tipos_BeverageSerializer(ModelSerializer):
    bebidas_ = Bebidas_Serializer(read_only=True)
    class Meta:
        model = beverages
        fields = ['NameBeverage', 'Beverage_description', 'Ingredients_Beverage', 'TiposBebidas']