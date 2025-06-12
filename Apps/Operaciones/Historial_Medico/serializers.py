from rest_framework.serializers import ModelSerializer, CharField

from Apps.Operaciones.Historial_Medico.models import medical_History

#Traer el serializador del expediente como puente para traer al paciente
from Apps.Operaciones.ExpedientePaciente.serializers import ExpedientPuentePacienteSerializer


class MedicalHistorySerializer(ModelSerializer):
    expediente_code = CharField(source='expedientP_FK.codeExpedient', read_only=True, label="Código de expediente")
    codigo_cama = CharField(source= 'bedFK.bedCode', read_only=True, label="Código de cama")
    codigo_Pedido = CharField(source='orderFk.codeOrder', read_only=True, label="Código de pedido")

    class Meta:
        model = medical_History
        fields = ['idMedicalHistory', 'codeHistory', 'expedientP_FK', 'expediente_code', 'bedFK', 'codigo_cama', 'orderFk', 'codigo_Pedido', 'dateHistory', 'active_Patient']


#Serializador para traer el expediente como puente para traer a la información del paciente
class PacienteActivoSerializer(ModelSerializer):
    paciente = ExpedientPuentePacienteSerializer(source='expedientP_FK', read_only=True)
    class Meta:
        model = medical_History
        fields = ['paciente', 'active_Patient']

class HistorialMedico7rows(ModelSerializer):
    expediente_code = CharField(source='expedientP_FK.codeExpedient', read_only=True, label="Código de expediente")
    codigo_cama = CharField(source= 'bedFK.bedCode', read_only=True, label="Código de cama")
    codigo_Pedido = CharField(source='orderFk.codeOrder', read_only=True, label="Código de pedido")

    class Meta:
        model = medical_History
        fields = ['idMedicalHistory', 'codeHistory', 'dateHistory', 'codigo_cama', 'expediente_code', 'codigo_Pedido', 'active_Patient']