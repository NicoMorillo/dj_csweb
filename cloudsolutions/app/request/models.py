from django.db import models

# Create your models here.

class Company(models.Model):
    comp_name = models.CharField(max_length=50)
    person_full_name = models.CharField(max_length=50)
    phone_num = models.IntegerField(max_length=11)
    email = models.EmailField()
    address = models.TextField()
