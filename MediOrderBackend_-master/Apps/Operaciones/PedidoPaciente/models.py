from django.db import models
from Apps.Seguridad.System_Admin.models import systemAdmin
from Apps.Operaciones.AgregadosC_B.models import aggregates_cb
# Create your models here.

class orderpatient(models.Model):
    idOrder= models.AutoField(primary_key=True)
    codeOrder= models.CharField(verbose_name= 'Codigo de pedido', max_length=10, unique=True)
    adminFK =models.ForeignKey(systemAdmin, verbose_name='Encargado del sistema', on_delete=models.PROTECT)
    aggregatesFK = models.ForeignKey(aggregates_cb, verbose_name='Agregados', on_delete=models.PROTECT)
    orderStatus = models.CharField(verbose_name="Estado del pedido", max_length=10)
    quantity = models.IntegerField(verbose_name="Cantidad")
    dateOrder = models.DateField(verbose_name="Fecha de creacion del pedido")

    class Meta:
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return f"{self.idOrder} - {self.codeOrder} - {self.orderStatus} - {self.quantity} - {self.dateOrder}"