from django.contrib import admin
from Apps.Operaciones.ExpedientePaciente.models import expedientPatient
# Register your models here.

@admin.register(expedientPatient)
class expedientPatientAdmin(admin.ModelAdmin):
    search_fields = ['idExpedient', 'codeExpedient']
    list_display = ['idExpedient', 'patientFK', 'conditionFK', 'detailDiseaseFK', 'codeExpedient', 'reasonConsult', 'diagnosis', 'treatment', 'dietaryRestrictions', 'dietaryPreferences', 'attedingPhysician']
