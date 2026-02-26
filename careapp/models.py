from django.db import models

# Create your models here.
class MyAppoinments(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    datetime = models.DateTimeField()
    Department = models.CharField(max_length=100)
    Doctor = models.CharField(max_length=100)
    Message = models.TextField()

class Patients(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    DOB = models.DateField()
    Age = models.IntegerField()
    contact = models.CharField(max_length=20)
    department = models.CharField(max_length=100)

class Doctor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    Phone = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
