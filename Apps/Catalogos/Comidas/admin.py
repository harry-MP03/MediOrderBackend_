from django.contrib import admin
from Apps.Catalogos.Comidas.models import foods
# Register your models here.

@admin.register(foods)
class FoodsAdmin(admin.ModelAdmin):
    search_fields = ['idFood', 'foodName']
    list_display = ['idFood', 'foodName', 'foodDescription', 'typeFoodFK', 'Ingredients_food']