from django.contrib import admin
from Apps.Operaciones.Historial_Medico.models import medical_History
# Register your models here.

@admin.register(medical_History)
class MedicalHistoryAdmin(admin.ModelAdmin):
    search_fields = ['idMedicalHistory', 'codeHistory']
    list_display = ['idMedicalHistory', 'expedientP_FK', 'bedFK', 'orderFk', 'codeHistory', 'dateHistory']
