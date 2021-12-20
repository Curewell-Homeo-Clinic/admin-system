import calendar
from datetime import date
from django.db.models import Sum
from patients.models import (
    Invoice,
    Appointment,
    Patient,
)

MONTHS = [
    'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December'
]


def get_current_year_stats() -> dict:
    year = date.today().year

    return {
        'patients':
        Patient.objects.filter(admitted_at__year=year).count(),
        'appointments':
        Appointment.objects.filter(date__year=year).count(),
        'sales':
        Invoice.objects.filter(date__year=year).aggregate(
            Sum('total_fee'))['total_fee__sum'],
    }


def get_year_dict() -> dict:
    year_dict = dict()

    for month in MONTHS:
        year_dict[month] = 0

    return year_dict


def get_month_sales(year: int, month: int) -> int:
    first_day = date(year, month, 1)
    last_day = date(year, month, calendar.monthrange(year, month)[1])

    sales = Invoice.objects.filter(
        date__range=[first_day, last_day]).aggregate(
            Sum('total_fee'))['total_fee__sum']

    if sales != None:
        return sales

    return 0