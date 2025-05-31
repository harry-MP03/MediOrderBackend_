from django.db import models
from Apps.Catalogos.TiposBebida.models import typeBeverage
# Create your models here.
class beverages(models.Model):
    idBeverages = models.AutoField(primary_key=True, unique=True)
    NameBeverage = models.CharField(verbose_name='Nombre de la bebida', max_length=60)
    Beverage_description = models.CharField(verbose_name='Descripción de la bebida', max_length=110)
    Ingredients_Beverage = models.CharField(verbose_name='Ingredientes de la bebida', max_length=120)
    typeBeveragesFK = models.ForeignKey(typeBeverage, verbose_name='Tipo de bebida', on_delete=models.PROTECT, default=None)

    class Meta:
        verbose_name_plural = 'Bebidas'

    def __str__(self):
        return f"{self.idBeverages} - {self.NameBeverage}"