from django.db import models

# Create your models here.
class typefood(models.Model):
    idTypeFood = models.AutoField(primary_key=True, unique=True)
    description_typefood = models.CharField(verbose_name='Descripción', max_length=100)

    class Meta:
        verbose_name_plural = 'Tipos de comida'

    def __str__(self):
        return f"{self.idTypeFood} - {self.description_typefood}"