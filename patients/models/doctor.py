from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


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
    address = models.CharField(max_length=200, blank=True, null=True)
    specialization = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{ self.first_name } { self.last_name }'
