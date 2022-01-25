from django.db import models
from request import Company
# Create your models here.

class Platform(models.Model):
    name = models.CharField(max_length=20) 

class Service(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=50)
    platform = models.CharField(max_length=20)
    cost_aprox = models.IntegerField()
    model = models.CharField(max_length=15)
    date_origin = models.DateField()
    request = models.ForeignKey(Company, null=True, blank=True, on_delete = models.CASCADA)
    platform = models.ManyToManyField(Platform)
