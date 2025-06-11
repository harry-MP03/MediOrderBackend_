from rest_framework.serializers import ModelSerializer, CharField

from Apps.Catalogos.Enfermedades.serializers import DiseasesForExpSerializer
from .models import detailDisease

class DetailDiseaseSerializer(ModelSerializer):
    nombreEnfermedad = CharField(source='diseaseFK.nameDisease', read_only=True, label = "Nombre de enfermedad")
    nombrePaciente = CharField(source='patient_dFK.namesPatient', read_only=True, label = "Nombre de paciente")
    apellido = CharField(source='patient_dFK.lastnamePatient', read_only=True, label = "Apellido")
    cedula = CharField(source='patient_dFK.cedulaPatient', read_only=True, label="Cedula")

    class Meta:
        model = detailDisease
        fields = ['idDetailDisease', 'diseaseFK', 'nombreEnfermedad', 'patient_dFK', 'nombrePaciente', 'apellido', 'cedula']

class DetailsDiseaseForExpedienteSerializer(ModelSerializer):
    info_Enfermedades = DiseasesForExpSerializer(source = 'diseaseFK', read_only=True)

    class Meta:
        model = detailDisease
        fields = ['info_Enfermedades']

class DetailDiseaseLookupSerializer(ModelSerializer):
    class Meta:
        model = detailDisease
        fields = ['idDetailDisease']