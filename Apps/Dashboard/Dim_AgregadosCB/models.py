from django.db import models

class DIM_AGREGADOS_CB_DEST(models.Model):
    idAggregates = models.IntegerField(primary_key=True)
    codeAggregates = models.CharField(max_length=100)
    foodName = models.CharField(max_length=60)
    description_typefood = models.CharField(max_length=100)
    Ingredients_food = models.CharField(max_length=120)
    NameBeverage = models.CharField(max_length=60)
    description_TypeBeverage = models.CharField(max_length=80)
    Ingredients_Beverage = models.CharField(max_length=120)

    class Meta:
        db_table = '[dbo].[DIM_AGREGADOS_CB_DEST]'
        managed = False
