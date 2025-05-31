from django.db import models
from Apps.Catalogos.TiposComida.models import typefood

# Create your models here.
class foods(models.Model):
    idFood = models.AutoField(primary_key=True, unique=True)
    foodName = models.CharField(verbose_name='Nombre de comida', max_length=60)
    foodDescription = models.CharField(verbose_name='Descripción de la comida', max_length=110)
    Ingredients_food = models.CharField(verbose_name='Ingredientes de la comida', max_length=120)
    typeFoodFK = models.ForeignKey(typefood, on_delete=models.CASCADE, verbose_name='Tipo de comida', default= None)

    class Meta:
        verbose_name_plural = 'Comidas'

    def __str__(self):
        return f"{self.idFood} - {self.foodName} - {self.foodDescription} - {self.Ingredients_food} - {self.typeFoodFK}"
