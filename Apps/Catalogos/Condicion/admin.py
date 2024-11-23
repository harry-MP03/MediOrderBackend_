from django.contrib import admin
from Apps.Catalogos.Condicion.models import condition_lvl
# Register your models here.

@admin.register(condition_lvl)
class condition_lvl(admin.ModelAdmin):
    search_fields = ['idcondition_lvl', 'ConditionName']
    list_display = ['idcondition_lvl', 'ConditionName']