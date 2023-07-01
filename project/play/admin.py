from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class DeviceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'number', 'kind', 'available','place', 'price')
    list_filter  = ('id', 'number', 'kind', 'available','place', 'price')
    search_fields= ('id', 'number', 'kind', 'available','place', 'price')
admin.site.register(Device, DeviceAdmin)

class RentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'device', 'duration', 'created_at', 'created_by')
    list_filter = ('id', 'device', 'duration', 'created_at', 'created_by')
    search_fields = ('id', 'device', 'duration', 'created_at', 'created_by')
admin.site.register(Rent, RentAdmin)

class OrderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'rent', 'name', 'price', 'created_at', 'created_by')
    list_filter = ('id', 'rent', 'name', 'price', 'created_at', 'created_by')
    search_fields = ('id', 'rent', 'name', 'price', 'created_at', 'created_by')

admin.site.register(Order, OrderAdmin)