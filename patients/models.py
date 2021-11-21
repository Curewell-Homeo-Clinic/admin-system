from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone_no = models.CharField(max_length=10, blank=True, null=True)
    age = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[MaxValueValidator(100),
                    MinValueValidator(1)])
    admitted_at = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'{ self.first_name } { self.last_name }'


class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone_no = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    age = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[MaxValueValidator(100),
                    MinValueValidator(1)])

    def __str__(self):
        return f'{ self.first_name } { self.last_name }'


class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
