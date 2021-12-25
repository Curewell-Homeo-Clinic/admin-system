from django.db import models
from .patient import Patient
from .doctor import Doctor
from decouple import config


class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    date = models.DateField(blank=True, null=True, auto_now_add=True)
    time = models.TimeField(auto_now_add=True, blank=True, null=True)
    consulation_fee = models.PositiveSmallIntegerField(
        blank=True, null=True, default=config('CONSULTATION_FEE'))
    medicine_fee = models.PositiveSmallIntegerField(blank=True, null=True)
    total_fee = models.PositiveSmallIntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        total_fee = self.consulation_fee + self.medicine_fee
        self.total_fee = total_fee
        super().save(*args, **kwargs)
