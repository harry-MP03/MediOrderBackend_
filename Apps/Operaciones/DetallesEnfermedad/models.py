from django.db import models
from Apps.Catalogos.Enfermedades.models import diseases
from Apps.Catalogos.Paciente.models import patient
# Create your models here.

class detailDisease(models.Model):
    idDetailDisease = models.AutoField(primary_key=True)
    diseaseFK = models.ForeignKey(diseases, verbose_name='Enfermedad', on_delete=models.PROTECT)
    patient_dFK = models.ForeignKey(patient, verbose_name='Paciente', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Detalles de enfermedad del paciente'

    def __str__(self):
        return f"{self.idDetailDisease}"