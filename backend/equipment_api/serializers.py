from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Equipment, UploadBatch

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['id', 'equipment_name', 'equipment_type', 'flowrate', 'pressure', 'temperature']

class UploadBatchSerializer(serializers.ModelSerializer):
    equipment = EquipmentSerializer(many=True, read_only=True)
    
    class Meta:
        model = UploadBatch
        fields = ['id', 'filename', 'total_equipment', 'avg_flowrate', 'avg_pressure', 'avg_temperature', 'created_at', 'equipment']

class CSVUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

class SummarySerializer(serializers.Serializer):
    total_equipment = serializers.IntegerField()
    equipment_types = serializers.DictField()
    avg_flowrate = serializers.FloatField()
    avg_pressure = serializers.FloatField()
    avg_temperature = serializers.FloatField()
    flowrate_range = serializers.DictField()
    pressure_range = serializers.DictField()
    temperature_range = serializers.DictField()
