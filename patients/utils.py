import calendar
from datetime import date, datetime
from django.db.models import Sum

from .models import Invoice


def get_current_month_sales():
    today = date.today()
    _, num_days = calendar.monthrange(today.year, today.month)
    first_day = date(today.year, today.month, 1)
    last_day = date(today.year, today.month, num_days)

    return Invoice.objects.filter(date__range=[first_day, last_day]).aggregate(
        Sum('total_fee'))['total_fee__sum']


MONTHS = [
    'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December'
]


def get_year_dict():
    year_dict = dict()

    for month in MONTHS:
        year_dict[month] = 0

    return year_dict


def get_month_dict(month: int, year: int) -> dict:
    month_dict = dict()

    num_days = calendar.monthrange(year, month)[1]

    for i in range(1, num_days + 1):
        month_dict[i] = 0

    return month_dict


def get_month_sales(year: int, month: int) -> int:
    first_day = date(year, month, 1)
    last_day = date(year, month, calendar.monthrange(year, month)[1])

    sales = Invoice.objects.filter(
        date__range=[first_day, last_day]).aggregate(
            Sum('total_fee'))['total_fee__sum']

    if sales != None:
        return sales

    return 0


def get_day_sales(date: datetime.date) -> int:
    sales = Invoice.objects.filter(date=date).aggregate(
        Sum('total_fee'))['total_fee__sum']

    if sales != None:
        return sales

    return 0
