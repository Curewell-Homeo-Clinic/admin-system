from .models import Appointment, Patient, Doctor, Invoice
from .utils import get_total_monthly_sales
from django.shortcuts import render
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
LOGIN_URL = getattr(settings, 'LOGIN_URL')


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
        'total_sales': get_total_monthly_sales(),
        'active': 'dashboard'
    }
    return render(request, 'dashboard/dashboard.html', context)


def get_data(request, *args, **kwargs):
    data = {
        "sales": get_total_sales(),
        "customers": 10,
    }
    return JsonResponse(data)

@login_required(login_url=LOGIN_URL)
def stats(request):
    context = {
        'active': 'stats'
    }
    return render(request, 'stats/stats.html', context)

def get_patient(filter_patient=None):
    if filter_patient:
        patients = Patient.objects.filter(first_name__icontains=filter_patient)
    else:
        patients = Patient.objects.all()

    return patients


@login_required(login_url=LOGIN_URL)
def patient_list(request):
    filter_patient = request.GET.get('filter_patient')
    if cache.get(f'patient_{filter_patient}'):
        patients = cache.get(f'patient_{filter_patient}')
    else:
        if filter_patient:
            patients = get_patient(filter_patient)
            cache.set(f'patient_{filter_patient}', patients, CACHE_TTL)
        else:
            patients = get_patient()

    context = {'patients': patients, 'active': 'patient'}
    return render(request, 'patients/patient_list.html', context=context)


@login_required(login_url=LOGIN_URL)
def patient_detail(request, pk):
    if cache.get(f'patient_{pk}'):
        patient = cache.get(f'patient_{pk}')
    else:
        patient = Patient.objects.get(pk=pk)
        cache.set(f'patient_{pk}', patient, CACHE_TTL)

    context = {
        'patient': patient,
        'patient_edit': f'/admin/patients/patient/{patient.id}/change',
        'patient_delete': f'/admin/patients/patient/{patient.id}/delete',
        'active': 'patient'
    }
    return render(request, 'patients/patient_detail.html', context)


def get_doctor(filter_doctor=None):
    if filter_doctor:
        doctors = Doctor.objects.filter(first_name__icontains=filter_doctor)
    else:
        doctors = Doctor.objects.all()

    return doctors


@login_required(login_url=LOGIN_URL)
def doctor_list(request):
    filter_doctor = request.GET.get('filter_doctor')
    if cache.get(f'doctor_{filter_doctor}'):
        doctors = cache.get(f'doctor_{filter_doctor}')
    else:
        if filter_doctor:
            doctors = get_doctor(filter_doctor)
            cache.set(f'doctor_{filter_doctor}', doctors, CACHE_TTL)
        else:
            doctors = get_doctor()

    context = {'doctors': doctors, 'active': 'doctor'}
    return render(request, 'doctors/doctor_list.html', context=context)


@login_required(login_url=LOGIN_URL)
def doctor_detail(request, pk):
    if cache.get(f'doctor_{pk}'):
        doctor = cache.get(f'doctor_{pk}')
    else:
        doctor = Doctor.objects.get(pk=pk)
        cache.set(f'doctor_{pk}', doctor, CACHE_TTL)

    context = {
        'doctor': doctor,
        'doctor_edit': f'/admin/patients/doctor/{doctor.id}/change',
        'doctor_delete': f'/admin/patients/doctor/{doctor.id}/delete',
        'active': 'doctor'
    }

    return render(request, 'doctors/doctor_detail.html', context)


def get_appointment(patient_name=None):
    if patient_name:
        patient = Patient.objects.filter(first_name__icontains=patient_name)
        appointments = Appointment.objects.filter(
            patient__in=patient).order_by('-id')
    else:
        appointments = Appointment.objects.all().order_by('-id')

    return appointments


@login_required(login_url=LOGIN_URL)
def appointment_list(request):
    filter_by_patient_name = request.GET.get('patient_name')
    if cache.get(f'appointment_{filter_by_patient_name}'):
        return cache.get(f'appointment_{filter_by_patient_name}')
    else:
        if filter_by_patient_name:
            appointments = get_appointment(patient_name=filter_by_patient_name)
            cache.set(f'appointment_{filter_by_patient_name}', appointments,
                      CACHE_TTL)
        else:
            appointments = get_appointment()

    context = {'appointments': appointments, 'active': 'appointment'}
    return render(request, 'appointments/appointments_list.html', context)


@login_required(login_url=LOGIN_URL)
def appointment_detail(request, pk):
    if cache.get(f'appointment{pk}'):
        appointment = cache.get(f'appointment{pk}')
    else:
        appointment = Appointment.objects.get(pk=pk)
        cache.set(f'appointment{pk}', appointment)

    context = {
        'appointment': appointment,
        'appointment_edit':
        f'/admin/patients/appointment/{appointment.id}/change',
        'appointment_delete':
        f'/admin/patients/appointment/{appointment.id}/delete',
        'active': 'appointment'
    }

    return render(request, 'appointments/appointment_detail.html', context)


def get_invoice(patient_name=None):
    if patient_name:
        patient = Patient.objects.filter(first_name__icontains=patient_name)
        invoices = Invoice.objects.filter(patient__in=patient).order_by('-id')
    else:
        invoices = Invoice.objects.all().order_by('-id')

    return invoices


@login_required(login_url=LOGIN_URL)
def invoice_list(request):
    filter_by_patient_name = request.GET.get('patient_name')
    if cache.get(f'invoice_{filter_by_patient_name}'):
        return cache.get(f'invoice_{filter_by_patient_name}')
    else:
        if filter_by_patient_name:
            invoices = get_invoice(patient_name=filter_by_patient_name)
            cache.set(f'invoice_{filter_by_patient_name}', invoices, CACHE_TTL)
        else:
            invoices = get_invoice()

    context = {'invoices': invoices, 'active': 'invoice'}
    return render(request, 'invoices/invoice_list.html', context)


@login_required(login_url=LOGIN_URL)
def invoice_detail(request, pk):
    if cache.get(f'invoice{pk}'):
        invoice = cache.get(f'invoice{pk}')
    else:
        invoice = Invoice.objects.get(pk=pk)
        cache.set(f'invoice{pk}', invoice)

    context = {
        'invoice': invoice,
        'invoice_edit': f'/admin/patients/invoice/{invoice.id}/change',
        'active': 'invoice'
    }

    return render(request, 'invoices/invoice_detail.html', context)


@login_required(login_url=LOGIN_URL)
def invoice_print(request, pk):
    if cache.get(f'invoice{pk}'):
        invoice = cache.get(f'invoice{pk}')
    else:
        invoice = Invoice.objects.get(pk=pk)
        cache.set(f'invoice{pk}', invoice)

    context = {'invoice': invoice, 'blank_row': range(6)}

    return render(request, 'invoices/print.html', context)
