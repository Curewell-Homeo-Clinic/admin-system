from django.db import models


class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name
