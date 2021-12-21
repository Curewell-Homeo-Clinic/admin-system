from datetime import date
from .models import Appointment, Patient, Doctor, Invoice
from patients.utils.stats.month import (
    get_current_month_stats,
    get_current_month_sales,
    get_month_dict,
    get_day_sales,
)

from patients.utils.stats.year import (get_month_sales, get_year_dict,
                                       get_current_year_stats, MONTHS)

from patients.utils.stats import get_gross_stats

from django.shortcuts import render
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.admin.views.decorators import staff_member_required

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
LOGIN_URL = getattr(settings, 'LOGIN_URL')


@staff_member_required
def get_monthly_sales_chart_data(request, year):
    sales_dict = get_year_dict()

    for month in MONTHS:
        sales_dict[month] = get_month_sales(year, MONTHS.index(month) + 1)

    return JsonResponse({
        'labels': list(sales_dict.keys()),
        'data': list(sales_dict.values())
    })


@staff_member_required
def get_daily_sales_chart_data(request, year, month):
    sales_dict = get_month_dict(month=month, year=year)

    for day in range(1, len(sales_dict) + 1):
        sales_dict[day] = get_day_sales(date(year, month, day))

    return JsonResponse({'data': list(sales_dict.values())})