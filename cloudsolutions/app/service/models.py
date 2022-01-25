from django.db import models
from app.request.models import Company
# Create your models here.

class Platform(models.Model):
    name = models.CharField(max_length=20) 

class Service(models.Model):
    
    name = models.CharField(max_length=50)
    platform = models.CharField(max_length=20)
    cost_aprox = models.IntegerField()
    model = models.CharField(max_length=15)
    date_origin = models.DateField()
    company = models.ForeignKey(Company, null=True, blank=True, on_delete = models.CASCADE)
    platform = models.ManyToManyField(Platform, blank=True)
