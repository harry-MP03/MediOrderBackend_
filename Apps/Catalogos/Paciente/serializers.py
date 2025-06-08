from rest_framework.serializers import ModelSerializer, CharField
from .models import patient

class PatientSerializer(ModelSerializer):
    class Meta:
        model = patient
        fields = ['namesPatient', 'lastnamePatient', 'cedulaPatient', 'genderPatient', 'agePatient', 'phonePatient']
