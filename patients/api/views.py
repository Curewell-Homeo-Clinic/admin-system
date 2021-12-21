from rest_framework import viewsets
from rest_framework import permissions

from .serializers import PatientSerializer, DoctorSerializer, AppointmentSerializer, InvoiceSerializer
from patients.models import Patient, Doctor, Appointment, Invoice

from datetime import date
from patients.utils.stats.month import (
    get_month_dict,
    get_day_sales,
)

from patients.utils.stats.year import (get_month_sales, get_year_dict, MONTHS)

from django.http import JsonResponse
from django.contrib.admin.views.decorators import staff_member_required


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


@staff_member_required
def get_monthly_sales(request, year):
    sales_dict = get_year_dict()

    for month in MONTHS:
        sales_dict[month] = get_month_sales(year, MONTHS.index(month) + 1)

    return JsonResponse({
        'labels': list(sales_dict.keys()),
        'data': list(sales_dict.values())
    })


@staff_member_required
def get_daily_sales(request, year, month):
    sales_dict = get_month_dict(month=month, year=year)

    for day in range(1, len(sales_dict) + 1):
        sales_dict[day] = get_day_sales(date(year, month, day))

    return JsonResponse({'data': list(sales_dict.values())})
