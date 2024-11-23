from django.contrib import admin
from Apps.Catalogos.Enfermedades.models import diseases
# Register your models here.

@admin.register(diseases)
class diseasesAdmin(admin.ModelAdmin):
    search_fields = ['idDisease', 'nameDisease']
    list_display = ['idDisease', 'nameDisease', 'typeDiseaseFK']