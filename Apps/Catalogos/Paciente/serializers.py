from rest_framework.serializers import ModelSerializer, CharField
from Apps.Operaciones.Historial_Medico.serializers import PacienteActivoSerializer
from .models import patient

class PatientSerializer(ModelSerializer):
    Paciente_Activo = PacienteActivoSerializer(read_only=True, label="Paciente Activo")
    class Meta:
        model = patient
        fields = ['namesPatient', 'lastnamePatient', 'cedulaPatient', 'genderPatient', 'agePatient', 'phonePatient', 'Paciente_Activo']
