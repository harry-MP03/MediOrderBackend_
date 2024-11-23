from django.db import models
from Apps.Catalogos.TiposEnfermedades.models import Typedisease
# Create your models here.
class diseases (models.Model):
    idDisease = models.AutoField(primary_key=True, unique=True)
    nameDisease = models.CharField(verbose_name='Nombre de la enfermedad', max_length=50)
    typeDiseaseFK =models.ForeignKey(Typedisease, verbose_name='Tipo de enfermedad', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural='Listado de Enfermedades'

    def __str__(self):
        return f"{self.idDisease} - {self.nameDisease}"