from django.contrib import admin
from Apps.Catalogos.TiposEnfermedades.models import Typedisease
# Register your models here.

@admin.register(Typedisease)
class TypediseaseAdmin(admin.ModelAdmin):
    search_fields = ['idtype', 'nametype']
    list_display = ['idtype', 'nametype']