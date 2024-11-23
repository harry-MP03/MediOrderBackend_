from django.contrib import admin
from Apps.Seguridad.System_Admin.models import systemAdmin
# Register your models here.

@admin.register(systemAdmin)
class systemAdmin(admin.ModelAdmin):
    search_fields = ['idAdmin', 'namesAdmin', 'Username']
    list_display = ['idAdmin', 'namesAdmin', 'lastNameAdmin', 'phoneAdmin', 'Username', 'password']
