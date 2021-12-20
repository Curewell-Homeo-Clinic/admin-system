from rest_framework import viewsets
from rest_framework import permissions

from .serializers import PatientSerializer, DoctorSerializer, AppointmentSerializer, InvoiceSerializer
from ..models import Patient, Doctor, Appointment, Invoice


class PatientsViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all().order_by('-admitted_at')
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]


class DoctorsViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]


class AppointmentsViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class InvoicesViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]
