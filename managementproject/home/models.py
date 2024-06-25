from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Doctors(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    department = models.ManyToManyField(Department)
    def __str__(self):
        return self.name

class Patients(models.Model):
    name = models.CharField(max_length=50)
    Address = models.TextField()
    Contact = models.CharField(max_length=50)
    Symptoms = models.TextField()
    Doctor = models.ForeignKey(Doctors,on_delete=models.CASCADE)
    Status = models.CharField(max_length=50)

    def __str__(self):
        return self.name



