
from django.db import models
from Apps.Catalogos.Paciente.models import patient
from Apps.Catalogos.Condicion.models import condition_lvl
from Apps.Operaciones.DetallesEnfermedad.models import detailDisease
# Create your models here.

class expedientPatient(models.Model):
    idExpedient = models.AutoField(primary_key=True)
    patientFK = models.ForeignKey(patient, verbose_name='Paciente', on_delete=models.PROTECT)
    conditionFK = models.ForeignKey(condition_lvl, verbose_name='Condición', on_delete=models.PROTECT)
    detailDiseaseFK = models.ForeignKey(detailDisease, verbose_name='Detalles de la enfermedad', on_delete=models.PROTECT)
    codeExpedient = models.CharField(verbose_name='Código del Expediente', max_length=60, unique=True)
    reasonConsult = models.CharField(verbose_name='Motivo de consulta', max_length=80)
    diagnosis = models.CharField(verbose_name='Diagnóstico', max_length=50)
    treatment = models.CharField(verbose_name='Tratamiento', max_length=60)
    dietaryRestrictions = models.CharField(verbose_name='Restricciones alimenticias', max_length=200)
    dietaryPreferences = models.CharField(verbose_name='Preferencias alimenticias', max_length=100)
    attedingPhysician = models.CharField(verbose_name='Médico a cargo', max_length=85)

    class Meta:
        verbose_name_plural = 'Expedientes de Pacientes'

    def __str__(self):
        return (f"{self.idExpedient} - {self.codeExpedient} - {self.reasonConsult} - {self.diagnosis} - "
                f"{self.treatment} - {self.dietaryRestrictions} - {self.dietaryPreferences} - {self.attedingPhysician}")