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

class Transaction(models.Model):
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=[('Success', 'Success'), ('Failed', 'Failed')])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone_number} - {self.amount} - {self.status}"