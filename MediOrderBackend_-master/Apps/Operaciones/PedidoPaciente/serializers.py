from rest_framework.serializers import ModelSerializer, CharField

from .models import orderpatient

#Para reportes de pedidos
from Apps.Operaciones.AgregadosC_B.serializers import AgregadosSoporte

class PedidosSoporteSerializer(ModelSerializer):
    agregados_Comida = AgregadosSoporte(source='aggregatesFK', read_only=True, label = 'Comidas agregados')

    class Meta:
        model = orderpatient
        fields = ['agregados_Comida']