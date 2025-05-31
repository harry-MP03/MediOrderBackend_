from django.contrib import admin
from Apps.Catalogos.TiposComida.models import typefood

# Register your models here.
@admin.register(typefood)
class typefoodAdmin(admin.ModelAdmin):
    search_fields = ['idTypeFood', 'description_typefood']
    list_display = ['idTypeFood', 'description_typefood']
