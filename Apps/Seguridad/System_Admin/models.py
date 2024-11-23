from django.db import models

# Create your models here.

class systemAdmin(models.Model):
    idAdmin = models.AutoField(primary_key=True, unique=True)
    namesAdmin = models.CharField(verbose_name='Nombres del encargado', max_length=60)
    lastNameAdmin = models.CharField(verbose_name='Apellidos del encargado', max_length=60)
    phoneAdmin = models.CharField(verbose_name='Teléfono del encargado', max_length=15)
    Username = models.CharField(verbose_name='Nombre de Usuario', max_length=15)
    password = models.CharField(verbose_name='Contraseña', max_length=15)

    class Meta:
        verbose_name_plural = 'Encargados'

    def __str__(self):
        return (f"{self.idAdmin} - {self.namesAdmin} - {self.lastNameAdmin} - {self.phoneAdmin} "
                f"- {self.Username} - {self.password}")