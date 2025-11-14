from django.contrib import admin
from .models import Equipment, UploadBatch

@admin.register(UploadBatch)
class UploadBatchAdmin(admin.ModelAdmin):
    list_display = ('filename', 'user', 'total_equipment', 'created_at')
    list_filter = ('created_at', 'user')
    search_fields = ('filename',)

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('equipment_name', 'equipment_type', 'flowrate', 'pressure', 'temperature')
    list_filter = ('equipment_type', 'batch')
    search_fields = ('equipment_name',)
