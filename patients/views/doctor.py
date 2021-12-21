from patients.models import Doctor
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from patients.views import LOGIN_URL, CACHE_TTL


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
