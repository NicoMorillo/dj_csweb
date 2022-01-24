from django.db import models

# Create your models here.


class Service(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=50)
    platform = models.CharField(max_length=20)
    cost_aprox = models.IntegerField()
    model = models.CharField(max_length=15)
    date_origin = models.DateField()
