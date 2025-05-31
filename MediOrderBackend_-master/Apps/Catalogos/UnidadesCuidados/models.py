from django.db import models

# Create your models here.
class Careunit(models.Model):
    idCareunit = models.AutoField(primary_key=True)
    nameCareUnit = models.CharField(verbose_name='Nombre de unidad de cuidado', max_length=250)

    class Meta:
        verbose_name_plural = 'Unidades de cuidado'

    def __str__(self):
        return f"{self.idCareunit} - {self.nameCareUnit}"