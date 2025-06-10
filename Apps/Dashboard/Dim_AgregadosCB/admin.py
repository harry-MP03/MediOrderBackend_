from django.contrib import admin
from Apps.Dashboard.Dim_AgregadosCB.models import DIM_AGREGADOS_CB_DEST
# Register your models here.

@admin.register(DIM_AGREGADOS_CB_DEST)
class DIMAGREGADOSCBAdmin(admin.ModelAdmin):
    search_fields = ['idAggregates']
    list_display = ['idAggregates', 'codeAggregates', 'foodName', 'description_typefood', 'Ingredients_food'
                    , 'NameBeverage', 'description_TypeBeverage', 'Ingredients_Beverage']