from rest_framework.serializers import ModelSerializer, CharField

from Apps.Operaciones.Historial_Medico.models import medical_History

#Para el reporte de pedidos
from Apps.Operaciones.ExpedientePaciente.serializers import ExpedienteReporteSerializer, ExpedienteSoporteSerializer
from Apps.Catalogos.Camas.serializers import CamaSoporteSerializer
from Apps.Operaciones.PedidoPaciente.serializers import PedidosSoporteSerializer

class MedicalHistorySerializer(ModelSerializer):
    expediente_code = CharField(source='expedientP_FK.codeExpedient', read_only=True, label="Código de expediente")
    codigo_cama = CharField(source= 'bedFK.bedCode', read_only=True, label="Código de cama")
    codigo_Pedido = CharField(source='orderFk.codeOrder', read_only=True, label="Código de pedido")

    class Meta:
        model = medical_History
        fields = ['codeHistory', 'expedientP_FK', 'expediente_code', 'bedFK', 'codigo_cama', 'orderFk', 'codigo_Pedido', 'dateHistory', 'active_Patient']

class PedidoDetalleSerializer(ModelSerializer):
    Info_Paciente = ExpedienteReporteSerializer(source='expedientP_FK', read_only=True, label = 'Nombre de Paciente - Cedula')
    Info_UnidadCuidado = CamaSoporteSerializer(source='bedFK', read_only=True, label = 'Unidad de Cuidado')
    Info_Comidas = PedidosSoporteSerializer(source='orderFk', read_only=True, label = 'Nombre de comidas y tipos')
    Info_Restricciones = ExpedienteSoporteSerializer(source='expedientP_FK', read_only=True, label = 'Restricciones')

    class Meta:
        model = medical_History
        fields = ['Info_Paciente', 'Info_UnidadCuidado', 'Info_Comidas', 'Info_Restricciones']