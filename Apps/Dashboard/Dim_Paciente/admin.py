from django.contrib import admin
from Apps.Dashboard.Dim_Paciente.models import DIM_PACIENTE_DEST
# Register your models here.

@admin.register(DIM_PACIENTE_DEST)
class DIMPACIENTELAdmin(admin.ModelAdmin):
    search_fields = ['PatientKey']
    list_display = ['PatientKey', 'namesPatient', 'lastnamePatient', 'agePatient', 'cedulaPatient'
                    , 'phonePatient', 'genderPatient']