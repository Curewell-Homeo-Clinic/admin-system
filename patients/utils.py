import calendar
from datetime import date
from django.db.models import Sum

from .models import Invoice

def get_total_monthly_sales():
	today = date.today()
	_, num_days = calendar.monthrange(today.year, today.month)
	first_day = date(today.year, today.month, 1)
	last_day = date(today.year, today.month, num_days)

	return Invoice.objects.filter(date__range=[first_day, last_day]).aggregate(Sum('total_fee'))['total_fee__sum']