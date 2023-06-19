from django.contrib import admin
from django.db import models
from django_json_widget.widgets import JSONEditorWidget

from .models import Printer, Check


@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    list_display = ['name', 'check_type', 'point_id']
    list_display_links = ['name']
    search_fields = ['name', 'check_type']
    list_filter = ['name', 'check_type']
    list_per_page = 25
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }


@admin.register(Check)
class CheckAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'status', 'type', 'printer_id']
    list_display_links = ['order_id', 'status']
    search_fields = ['status', 'type', 'printer_id']
    list_filter = ['status', 'type', 'printer_id']
    list_per_page = 25
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }
