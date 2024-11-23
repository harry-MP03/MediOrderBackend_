from django.db import models

# Create your models here.
class Typedisease(models.Model):
    idtype=models.AutoField(primary_key=True, unique=True)
    nametype=models.CharField(verbose_name='Nombre del tipo de enfermedad', max_length=60)

    class Meta:
        verbose_name_plural = 'Tipos de enfermedad'

    def __str__(self):
        return f"{self.idtype} - {self.nametype}"