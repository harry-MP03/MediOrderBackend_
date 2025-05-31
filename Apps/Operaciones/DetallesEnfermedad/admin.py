from django.contrib import admin
from django.views.generic import detail

from Apps.Operaciones.DetallesEnfermedad.models import detailDisease
# Register your models here.

@admin.register(detailDisease)
class detailDiseaseAdmin(admin.ModelAdmin):
    search_fields = ['idDetailDisease']
    list_display = ['idDetailDisease', 'diseaseFK', 'patient_dFK']