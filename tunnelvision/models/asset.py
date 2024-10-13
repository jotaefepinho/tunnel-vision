from django.db import models

class Asset(models.Model):
    symbol = models.CharField(max_length=10)

class MonitoringConfig(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)

    lower_bound = models.DecimalField(max_digits=10, decimal_places=2)
    upper_bound = models.DecimalField(max_digits=10, decimal_places=2)
    
    frequency = models.IntegerField()