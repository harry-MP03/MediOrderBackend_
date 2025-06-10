from django.db import models

class DIM_SYSTEM_ADMIN_DEST(models.Model):
    idAdmin =models.IntegerField()
    namesAdmin = models.CharField(max_length=60)
    lastNameAdmin =models.CharField(max_length=60)
    phoneAdmin = models.CharField(max_length=15)
    Username = models.CharField(max_length=80)

    class Meta:
        db_table = '[dbo].[DIM_SYSTEM_ADMIN_DEST]'
        managed = False
