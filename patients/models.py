from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from patients.send_sms import send_sms
from .send_mail import send_mail


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
    email= models.EmailField(blank=True, null=True)
    address= models.CharField(max_length=200, blank=True, null=True)
    occupation= models.CharField(max_length=100, blank=True, null=True)

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
    address= models.CharField(max_length=200, blank=True, null=True)
    specialization= models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{ self.first_name } { self.last_name }'


class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        send_mail(self, 'new')
        # send_sms(self, self.patient.phone_no, 'Appointment Added.')
        super().save(*args, **kwargs)

    def update(self, *args, **kwargs):
        send_mail(self, 'update')
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        send_mail(self, 'cancel')
        super().save(*args, **kwargs)
