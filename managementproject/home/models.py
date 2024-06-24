from django.db import models

# Create your models here.

class Doctors(models.Model):
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
