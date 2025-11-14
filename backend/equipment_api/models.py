from django.db import models
from django.contrib.auth.models import User

class UploadBatch(models.Model):
    """Stores metadata for each upload batch"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    filename = models.CharField(max_length=255)
    total_equipment = models.IntegerField(default=0)
    avg_flowrate = models.FloatField(default=0)
    avg_pressure = models.FloatField(default=0)
    avg_temperature = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.filename} - {self.created_at}"

class Equipment(models.Model):
    """Stores equipment data from CSV uploads"""
    EQUIPMENT_TYPES = [
        ('Centrifugal Pump', 'Centrifugal Pump'),
        ('Heat Exchanger', 'Heat Exchanger'),
        ('Rotary Compressor', 'Rotary Compressor'),
        ('Particulate Filter', 'Particulate Filter'),
        ('Batch Reactor', 'Batch Reactor'),
        ('Distillation Column', 'Distillation Column'),
        ('Gear Pump', 'Gear Pump'),
        ('Bag Filter', 'Bag Filter'),
        ('Crystallizer', 'Crystallizer'),
        ('Wet Scrubber', 'Wet Scrubber'),
        ('Centrifuge', 'Centrifuge'),
        ('Continuous Reactor', 'Continuous Reactor'),
    ]
    
    batch = models.ForeignKey(UploadBatch, on_delete=models.CASCADE, related_name='equipment')
    equipment_name = models.CharField(max_length=255)
    equipment_type = models.CharField(max_length=100, choices=EQUIPMENT_TYPES)
    flowrate = models.FloatField()
    pressure = models.FloatField()
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['equipment_name']
        indexes = [
            models.Index(fields=['batch', 'equipment_type']),
        ]
    
    def __str__(self):
        return self.equipment_name
