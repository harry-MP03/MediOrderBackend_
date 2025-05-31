from django.db import models

from Apps.Catalogos.Bebidas.models import beverages
from Apps.Catalogos.Comidas.models import foods
# Create your models here.

class aggregates_cb(models.Model):
    idAggregates = models.AutoField(primary_key=True)
    codeAggregates = models.CharField(verbose_name='Código de agregados', max_length=100, unique=True)
    foodFK = models.ForeignKey(foods, verbose_name='Comida agregada', on_delete=models.PROTECT)
    beverageFK = models.ForeignKey(beverages, verbose_name='Bebida agregada', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural= 'Agregados'

    def __str__(self):
        return f"{self.idAggregates} - {self.codeAggregates}"