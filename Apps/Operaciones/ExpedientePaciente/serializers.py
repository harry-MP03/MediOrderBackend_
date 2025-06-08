from rest_framework.serializers import ModelSerializer, CharField

from .models import expedientPatient
from Apps.Catalogos.Enfermedades.models import diseases
from Apps.Operaciones.DetallesEnfermedad.serializers import DetailsDiseaseForExpedienteSerializer


class Enfermedades_ParaExpedienteSerializer(ModelSerializer):
    nombreTipo_Enfermedad = CharField(source='typeDiseaseFK.nametype', label='Nombre de tipo de enfermedad',read_only=True)

    class Meta:
        model = diseases
        fields = ['nameDisease', 'nombreTipo_Enfermedad']

class ExpedienteSerializer(ModelSerializer):
    nombre_paciente = CharField(source='patientFK.namesPatient', label='Nombre del paciente' ,read_only=True)
    apellido_paciente = CharField(source='patientFK.lastnamePatient', label='Apellido del paciente' ,read_only=True)
    condicionDel_Paciente = CharField(source='conditionFK.ConditionName', label='Condicion del paciente' ,read_only=True)
    enfermedades_detalles = DetailsDiseaseForExpedienteSerializer(source = 'detailDiseaseFK', read_only=True, label='Enfermedades')

    class Meta:
        model = expedientPatient
        fields = ['codeExpedient', 'patientFK','nombre_paciente', 'apellido_paciente', 'conditionFK','condicionDel_Paciente', 'detailDiseaseFK','enfermedades_detalles', 'reasonConsult', 'diagnosis', 'treatment', 'dietaryRestrictions', 'dietaryPreferences', 'attedingPhysician']
