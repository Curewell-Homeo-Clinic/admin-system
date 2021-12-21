from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from patients.models import Appointment, Patient
from django.conf import settings
from patients.utils.stats.month import get_current_month_sales
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import render

LOGIN_URL = getattr(settings, 'LOGIN_URL')
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@login_required(login_url=LOGIN_URL)
def dashboard(request):
    if cache.get('recent_patients'):
        recent_patients = cache.get('recent_patients')
    else:
        recent_patients = Patient.objects.all().order_by('-id')[:10]
        cache.set('recent_patients', recent_patients, CACHE_TTL)

    if cache.get('recent_appointments'):
        recent_appointments = cache.get('recent_appointments')
    else:
        recent_appointments = Appointment.objects.all().order_by('-id')[:10]
        cache.set('recent_appointments', recent_appointments, CACHE_TTL)

    context = {
        'recent_patients': recent_patients,
        'recent_appointments': recent_appointments,
        'total_patients': Patient.objects.all().count(),
        'total_appointments': Appointment.objects.all().count(),
        'total_sales': get_current_month_sales(),
        'active': 'dashboard'
    }
    return render(request, 'dashboard/dashboard.html', context)