from django.db import models

# Create your models here.
class ras_info(models.Model):
    temperature = models.FloatField(max_length=255)
    humidity = models.FloatField(max_length=255)
    cpu_temperature = models.FloatField(max_length=255)
    cpu_useage = models.FloatField(max_length=255)
    harddrive_useage = models.FloatField(max_length=255)
    data = models.DateTimeField()