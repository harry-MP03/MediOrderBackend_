from django.contrib import admin
from Apps.Dashboard.Fact_PedidoPaciente.models import H_PEDIDOS_PACIENTE_DEST
# Register your models here.

@admin.register(H_PEDIDOS_PACIENTE_DEST)
class HPEDIDOSAdmin(admin.ModelAdmin):
    search_fields = ['codeOrder']
    list_display = ['codeOrder', 'quantity', 'aggregatesFK_id', 'adminFK_id', 'idMedicalHistory'
                    , 'idpatient', 'Result_TiempoKey']
