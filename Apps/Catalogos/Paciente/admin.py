from django.contrib import admin
from Apps.Catalogos.Paciente.models import patient
# Register your models here.

@admin.register(patient)
class PatientAdmin(admin.ModelAdmin):
    search_fields = ['idpatient', 'namesPatient', 'lastnamePatient', 'cedulaPatient']
    list_display = ['idpatient', 'namesPatient', 'lastnamePatient', 'cedulaPatient', 'genderPatient', 'agePatient', 'phonePatient']