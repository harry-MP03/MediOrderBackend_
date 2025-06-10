from django.db import models

from Apps.Dashboard.Dim_Paciente.models import DIM_PACIENTE_DEST

class DIM_HISTORIAL_MEDICO_DEST(models.Model):
    idMedicalHistory = models.IntegerField(primary_key=True)
    dateHistory = models.DateField()
    codeHistory = models.CharField(max_length=60)
    bedCode = models.CharField(max_length=100, unique=True)
    NameCareUnit = models.CharField(max_length=250)
    CodeExpedient = models.CharField(max_length=60)
    ReasonConsult = models.CharField(max_length=80)
    Diagnosis_Evento = models.CharField(max_length=50)
    Treatment_Evento = models.CharField(max_length=60)
    dietaryRestrictions = models.CharField(max_length=200)
    dietaryPreferences = models.CharField(max_length=100)
    attedingPhysician = models.CharField(max_length=85)
    ConditionName = models.CharField(max_length=20)
    IdPatient_OLTP = models.ForeignKey(DIM_PACIENTE_DEST, on_delete=models.PROTECT, db_column='IdPatient_OLTP')

    class Meta:
        db_table = '[dbo].[DIM_HISTORIAL_MEDICO_DEST]'
        managed = False

