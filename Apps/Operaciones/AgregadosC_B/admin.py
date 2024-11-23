from django.contrib import admin
from Apps.Operaciones.AgregadosC_B.models import aggregates_cb
# Register your models here.

@admin.register(aggregates_cb)
class aggregates_cbAdmin(admin.ModelAdmin):
    search_fields = ['idAggregates', 'codeAggregates']
    list_display = ['idAggregates', 'codeAggregates', 'foodFK', 'beverageFK']