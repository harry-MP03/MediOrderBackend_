from rest_framework.serializers import ModelSerializer, CharField

from Apps.Catalogos.Paciente.models import patient
from Apps.Operaciones.Historial_Medico.models import medical_History


class MedicalHistorySerializer(ModelSerializer):
    expediente_code = CharField(source='expedientP_FK.codeExpedient', read_only=True, label="Código de expediente")
    codigo_cama = CharField(source= 'bedFK.bedCode', read_only=True, label="Código de cama")
    codigo_Pedido = CharField(source='orderFk.codeOrder', read_only=True, label="Código de pedido")

    class Meta:
        model = medical_History
        fields = ['codeHistory', 'expedientP_FK', 'expediente_code', 'bedFK', 'codigo_cama', 'orderFk', 'codigo_Pedido', 'dateHistory', 'active_Patient']

class PacienteActivoSerializer(ModelSerializer):
    class Meta:
        model = medical_History
        fields = ['active_Patient']