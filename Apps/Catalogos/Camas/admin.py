from django.contrib import admin
from Apps.Catalogos.Camas.models import beds
# Register your models here.

@admin.register(beds)
class BedsAdmin(admin.ModelAdmin):
    search_fields = ['idbed', 'bedCode']
    list_display = ['idbed', 'bedCode', 'CareUnitFK']