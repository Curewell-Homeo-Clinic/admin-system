from patients.models import Appointment, Patient
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from patients.views import LOGIN_URL, CACHE_TTL


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
