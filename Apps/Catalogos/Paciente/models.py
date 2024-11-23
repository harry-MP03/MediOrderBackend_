from django.db import models

# Create your models here.
class patient(models.Model):
    idpatient = models.AutoField(primary_key=True, unique=True)
    namesPatient = models.CharField(verbose_name='Nombres del paciente', max_length=60)
    lastnamePatient = models.CharField(verbose_name='Apellidos del paciente', max_length=60)
    cedulaPatient = models.CharField(verbose_name='Cédula del paciente', max_length=14)
    genderPatient = models.CharField(verbose_name='Sexo del paciente', max_length=10)
    agePatient = models.IntegerField(verbose_name='Age del paciente')
    phonePatient = models.CharField(verbose_name='Teléfono del paciente', max_length=15)

    class Meta:
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return (f"{self.idpatient} - {self.namesPatient} - {self.lastnamePatient} - {self.cedulaPatient} - "
                f"{self.genderPatient} - {self.agePatient} - {self.phonePatient}")