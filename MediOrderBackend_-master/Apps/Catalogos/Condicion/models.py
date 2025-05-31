from django.db import models

# Create your models here.
class condition_lvl(models.Model):
    idcondition_lvl = models.AutoField(primary_key=True, unique=True)
    ConditionName = models.CharField(verbose_name='Nombre de condition', max_length=20)

    class Meta:
        verbose_name_plural = 'Condiciones'

    def __str__(self):
        return f"{self.idcondition_lvl} - {self.ConditionName}"