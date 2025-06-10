from django.contrib import admin
from Apps.Dashboard.Dim_Tiempo.models import DIM_TIEMPO_DEST
# Register your models here.

@admin.register(DIM_TIEMPO_DEST)
class DIMTIEMPOAdmin(admin.ModelAdmin):
    search_fields = ['TiempoKey']
    list_display = ['TiempoKey', 'FechaCompleta', 'Anio', 'MesNumero', 'NombreMes'
                    , 'DiaDelMes', 'DiaSemanaNumero', 'NombreDiaSemana', 'TrimestreNumero', 'NombreTrimestre',
                    'SemanaDelAnioNumero', 'EsFinDeSemana', 'NombreEsFinDeSemana']
