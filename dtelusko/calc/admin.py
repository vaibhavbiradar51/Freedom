from django.contrib import admin
from .models import Log
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Log)
class ViewAdmin(ImportExportModelAdmin):
    list_display=('idNumber','in_time','out_time')