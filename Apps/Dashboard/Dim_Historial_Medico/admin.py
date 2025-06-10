from django.contrib import admin
from Apps.Dashboard.Dim_Historial_Medico.models import DIM_HISTORIAL_MEDICO_DEST
# Register your models here.

@admin.register(DIM_HISTORIAL_MEDICO_DEST)
class DIMHISTORIALAdmin(admin.ModelAdmin):
    search_fields = ['idMedicalHistory']
    list_display = ['idMedicalHistory', 'dateHistory', 'codeHistory', 'bedCode', 'NameCareUnit'
                    , 'CodeExpedient', 'ReasonConsult', 'Diagnosis_Evento', 'Treatment_Evento', 'dietaryRestrictions',
                    'dietaryPreferences', 'attedingPhysician', 'ConditionName', 'IdPatient_OLTP']