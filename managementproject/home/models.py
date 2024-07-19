from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Doctors(models.Model):
    img= models.ImageField(upload_to='picture')
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

class DoctorReport(models.Model):
    patient = models.OneToOneField(Patients, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    update_date = models.DateField()
    admission_details = models.DateField()
    medicine = models.TextField()
    conclusion = models.TextField()

    def __str__(self):
        return f'Doctor Report for {self.patient.name}'

class Discharge(models.Model):
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    discharge_date = models.DateField()
    discharge_summary = models.TextField()

    def __str__(self):
        return f'Discharge Summary for {self.patient.name}'



