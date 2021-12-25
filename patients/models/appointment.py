from django.db import models
# from patients.utils.send_sms import send_sms
from patients.utils.send_mail import send_mail
from .patient import Patient
from .doctor import Doctor


class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        send_mail(self, 'new')
        # message = f'Dear { self.patient.first_name } { self.patient.last_name } your appointment with Dr. {self.doctor.first_name} {self.doctor.first_name} has been booked successfully for {self.date} at {self.time}'
        # send_sms(self, self.patient.phone_no, message)
        super().save(*args, **kwargs)

    def update(self, *args, **kwargs):
        send_mail(self, 'update')
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        send_mail(self, 'cancel')
        # message = f'Dear { self.patient.first_name } { self.patient.last_name } your appointment with Dr. {self.doctor.first_name} {self.doctor.first_name} has been cancelled for {self.date} at {self.time}'
        # send_sms(self, self.patient.phone_no, message)
        super().save(*args, **kwargs)
