from django.db import models

# Create your models here.

class Company(models.Model):
    comp_name = models.CharField(max_length=50)
    person_full_name = models.CharField(max_length=50)
    phone_num = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
