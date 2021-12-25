import calendar
from datetime import date, datetime
from django.db.models import Sum
from patients.models import (
    Invoice,
    Appointment,
    Patient,
)


def get_current_month_sales() -> int:
    today = date.today()
    _, num_days = calendar.monthrange(today.year, today.month)
    first_day = date(today.year, today.month, 1)
    last_day = date(today.year, today.month, num_days)

    return Invoice.objects.filter(date__range=[first_day, last_day]).aggregate(
        Sum('total_fee'))['total_fee__sum']


def get_current_month_appointments() -> int:
    today = date.today()
    _, num_days = calendar.monthrange(today.year, today.month)
    first_day = date(today.year, today.month, 1)
    last_day = date(today.year, today.month, num_days)

    return Appointment.objects.filter(
        date__range=[first_day, last_day]).count()


def get_current_month_patients() -> int:
    today = date.today()
    _, num_days = calendar.monthrange(today.year, today.month)
    first_day = date(today.year, today.month, 1)
    last_day = date(today.year, today.month, num_days)

    return Patient.objects.filter(
        admitted_at__range=[first_day, last_day]).count()


def get_current_month_stats() -> dict:
    return {
        'sales': get_current_month_sales(),
        'appointments': get_current_month_appointments(),
        'patients': get_current_month_patients(),
    }


def get_month_dict(month: int, year: int) -> dict:
    month_dict = dict()

    num_days = calendar.monthrange(year, month)[1]

    for i in range(1, num_days + 1):
        month_dict[i] = 0

    return month_dict


def get_day_sales(date: datetime.date) -> int:
    sales = Invoice.objects.filter(date=date).aggregate(
        Sum('total_fee'))['total_fee__sum']

    if sales != None:
        return sales

    return 0