from django.db import models

from Apps.Dashboard.Dim_Paciente.models import DIM_PACIENTE_DEST
from Apps.Dashboard.Dim_Tiempo.models import DIM_TIEMPO_DEST
from Apps.Dashboard.Dim_systemadmin.models import DIM_SYSTEM_ADMIN_DEST
from Apps.Dashboard.Dim_AgregadosCB.models import DIM_AGREGADOS_CB_DEST
from Apps.Dashboard.Dim_Historial_Medico.models import DIM_HISTORIAL_MEDICO_DEST

class H_PEDIDOS_PACIENTE_DEST(models.Model):
    codeOrder = models.CharField(max_length=10)
    quantity = models.IntegerField()
    aggregatesFK_id = models.ForeignKey(DIM_AGREGADOS_CB_DEST, on_delete=models.PROTECT, db_column='aggregatesFK_id')
    adminFK_id = models.ForeignKey(DIM_SYSTEM_ADMIN_DEST, on_delete=models.PROTECT, db_column='adminFK_id')
    idMedicalHistory = models.ForeignKey(DIM_HISTORIAL_MEDICO_DEST, on_delete=models.PROTECT, db_column='idMedicalHistory')
    idpatient = models.ForeignKey(DIM_PACIENTE_DEST, on_delete=models.PROTECT, db_column='idpatient')
    Result_TiempoKey = models.ForeignKey(DIM_TIEMPO_DEST, on_delete=models.PROTECT, db_column='Result_TiempoKey')

    class Meta:
        db_table = '[dbo].[H_PEDIDOS_PACIENTE_DEST]'
        managed = False
