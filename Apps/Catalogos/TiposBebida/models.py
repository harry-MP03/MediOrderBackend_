from django.db import models

# Create your models here.
class typeBeverage(models.Model):
    id_typeBeverage = models.AutoField(primary_key=True, unique=True)
    description_TypeBeverage = models.CharField(verbose_name="Descripción", max_length=80)

    class Meta:
        verbose_name_plural = "Tipos de bebida"

    def __str__(self):
        return f"{self.id_typeBeverage} - {self.description_TypeBeverage}"