from django.db import models


class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone_no = models.CharField(max_length=10, blank=True, null=True)
    age = models.IntegerField()
    admitted_at = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'{ self.first_name } { self.last_name }'
