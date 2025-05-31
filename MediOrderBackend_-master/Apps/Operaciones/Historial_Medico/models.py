from django.db import models
from Apps.Operaciones.ExpedientePaciente.models import expedientPatient
from Apps.Catalogos.Camas.models import beds
from Apps.Operaciones.PedidoPaciente.models import orderpatient

# Create your models here.

class medical_History(models.Model):
    idMedicalHistory = models.AutoField(primary_key=True)
    expedientP_FK = models.ForeignKey(expedientPatient, verbose_name='Expediente del paciente', on_delete=models.PROTECT)
    bedFK = models.ForeignKey(beds, verbose_name='Cama del paciente', on_delete=models.PROTECT, related_name='historiales_medicos')
    orderFk = models.ForeignKey(orderpatient, verbose_name= 'Pedido del Paciente', on_delete=models.PROTECT, null = True)
    codeHistory = models.CharField(verbose_name='Código de historial', max_length=60, unique=True)
    dateHistory = models.DateField(verbose_name='Fecha del historial', auto_now=True)
    active_Patient = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Historiales Médicos'

    def __str__(self):
        return (f"{self.idMedicalHistory} - {self.expedientP_FK} - {self.bedFK} - {self.orderFk} -"
                f" {self.codeHistory} - {self.dateHistory} - {self.active_Patient}")