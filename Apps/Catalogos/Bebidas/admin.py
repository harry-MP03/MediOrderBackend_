from django.contrib import admin
from Apps.Catalogos.Bebidas.models import beverages
# Register your models here.

@admin.register(beverages)
class BeveragesAdmin(admin.ModelAdmin):
    search_fields = ['idBeverages', 'NameBeverage']
    list_display = ['idBeverages', 'NameBeverage', 'Beverage_description', 'typeBeveragesFK','Ingredients_Beverage']