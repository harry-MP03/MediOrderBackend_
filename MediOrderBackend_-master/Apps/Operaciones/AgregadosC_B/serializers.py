from rest_framework.serializers import ModelSerializer, CharField

from .models import aggregates_cb

#Para los reportes de pedidos
from Apps.Catalogos.Comidas.serializers import ComidaSoporteSerializer

#Para los reportes de pedidos
class AgregadosSoporte(ModelSerializer):
    Comidas = ComidaSoporteSerializer(source='foodFK', read_only=True, label = 'Comidas')

    class Meta:
        model = aggregates_cb
        fields = ['Comidas']