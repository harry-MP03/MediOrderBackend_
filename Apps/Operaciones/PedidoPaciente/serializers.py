from rest_framework.serializers import ModelSerializer, CharField

from .models import orderpatient

class PedidoPacienteSerializer(ModelSerializer):
    userNameAdmin = CharField(source='adminFK.Username', read_only=True, label='Nombre de usuario')
    codigoAgregados = CharField(source='aggregatesFK.codeAggregates', read_only=True, label='Codigo de agregados')

    class Meta:
        model = orderpatient
        fields = ['idOrder', 'codeOrder', 'adminFK', 'userNameAdmin', 'aggregatesFK', 'codigoAgregados'
                ,'orderStatus', 'quantity', 'dateOrder']