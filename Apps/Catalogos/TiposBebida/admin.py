from django.contrib import admin
from Apps.Catalogos.TiposBebida.models import typeBeverage

# Register your models here.
@admin.register(typeBeverage)
class typeBeverageAdmin(admin.ModelAdmin):
    search_fields = ['id_typeBeverage', 'description_TypeBeverage']
    list_display = ['id_typeBeverage', 'description_TypeBeverage']
