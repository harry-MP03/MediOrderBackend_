from django.contrib import admin
from Apps.Operaciones.PedidoPaciente.models import orderpatient
# Register your models here.

@admin.register(orderpatient)
class orderpatientAdmin(admin.ModelAdmin):
    search_fields = ['idOrder', 'codeOrder']
    list_display = ['idOrder', 'codeOrder', 'adminFK', 'aggregatesFK', 'orderStatus', 'quantity', 'dateOrder']
