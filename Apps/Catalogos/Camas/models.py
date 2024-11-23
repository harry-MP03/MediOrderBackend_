from django.db import models
from Apps.Catalogos.UnidadesCuidados.models import Careunit
# Create your models here.
class beds(models.Model):
    idbed = models.AutoField(primary_key=True)
    bedCode = models.CharField(verbose_name='Código de cama', max_length=10, unique=True)
    CareUnitFK = models.ForeignKey(Careunit, verbose_name='Unidad de cuidado', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Camas'

    def __str__(self):
        return f"{self.idbed} - {self.bedCode}"
