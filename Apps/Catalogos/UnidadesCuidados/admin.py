from django.contrib import admin
from Apps.Catalogos.UnidadesCuidados.models import Careunit
# Register your models here.

@admin.register(Careunit)
class CareunitAdmin(admin.ModelAdmin):
    search_fields = ['idCareunit', 'nameCareUnit']
    list_display = ['idCareunit', 'nameCareUnit']