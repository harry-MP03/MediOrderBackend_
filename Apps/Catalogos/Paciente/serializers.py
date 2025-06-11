from rest_framework.serializers import ModelSerializer, CharField
from .models import patient

class PatientSerializer(ModelSerializer):
    class Meta:
        model = patient
        fields = ['idpatient', 'namesPatient', 'lastnamePatient', 'cedulaPatient', 'genderPatient', 'agePatient', 'phonePatient']

class PacienteDetalleEnfermedadSerializer(ModelSerializer):
    class Meta:
        model = patient
        fields = ['lastnamePatient', 'cedulaPatient']

class PacientesLookupsSerializers(ModelSerializer):
    class Meta:
        model = patient
        fields = ['idpatient', 'cedulaPatient']
