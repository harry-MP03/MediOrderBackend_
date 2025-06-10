from django.contrib import admin
from Apps.Dashboard.Dim_systemadmin.models import DIM_SYSTEM_ADMIN_DEST
# Register your models here.

@admin.register(DIM_SYSTEM_ADMIN_DEST)
class DIMSYSTEMLAdmin(admin.ModelAdmin):
    search_fields = ['idAdmin']
    list_display = ['idAdmin', 'namesAdmin', 'lastNameAdmin', 'phoneAdmin', 'Username']
