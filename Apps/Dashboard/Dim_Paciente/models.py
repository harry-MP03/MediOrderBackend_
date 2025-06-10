from django.db import models

class DIM_PACIENTE_DEST(models.Model):
    PatientKey = models.IntegerField(primary_key=True)
    namesPatient = models.CharField(max_length=60)
    lastnamePatient = models.CharField(max_length=60)
    agePatient = models.IntegerField()
    cedulaPatient = models.CharField(max_length=14)
    phonePatient = models.CharField(max_length=15)
    genderPatient = models.CharField(max_length=10)

    class Meta:
        db_table = '[dbo].[DIM_PACIENTE_DEST]'
        managed = False