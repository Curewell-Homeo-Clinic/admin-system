from django.db.models import Sum
from patients.models import (
    Invoice,
    Appointment,
    Patient,
)


def get_gross_stats() -> dict:
    return {
        'patients':
        Patient.objects.all().count(),
        'appointments':
        Appointment.objects.all().count(),
        'sales':
        Invoice.objects.all().aggregate(Sum('total_fee'))['total_fee__sum'],
        'invoices':
        Invoice.objects.all().count(),
    }