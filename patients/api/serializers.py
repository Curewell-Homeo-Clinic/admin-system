from rest_framework import serializers
from django_restql.mixins import DynamicFieldsMixin

from ..models import Patient, Doctor, Appointment, Invoice


class PatientSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class DoctorSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class AppointmentSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class InvoiceSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'
