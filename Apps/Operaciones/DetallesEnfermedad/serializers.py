from rest_framework.serializers import ModelSerializer, CharField

from Apps.Catalogos.Enfermedades.serializers import DiseasesForExpSerializer
from .models import detailDisease

class DetailDiseaseSerializer(ModelSerializer):
    nombreEnfermedad = CharField(source='diseaseFK.nameDisease', read_only=True, label = "Nombre de enfermedad")
    nombrePaciente = CharField(source='patient_dFK.namesPatient', read_only=True, label = "Nombre de paciente")
    apellidoPaciente = CharField(source='patient_dFk.lastnamePatient', read_only=True, label = "Apellido de paciente")
    cedulaPaciente = CharField(source='patient_dFk.cedulaPatient', read_only=True, label = "Cedula de paciente")

    class Meta:
        model = detailDisease
        fields = ['nombreEnfermedad', 'nombrePaciente', 'apellidoPaciente', 'cedulaPaciente']

class DetailsDiseaseForExpedienteSerializer(ModelSerializer):
    info_Enfermedades = DiseasesForExpSerializer(source = 'diseaseFK', read_only=True)

    class Meta:
        model = detailDisease
        fields = ['info_Enfermedades']