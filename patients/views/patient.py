from patients.models import Patient
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.shortcuts import render
from patients.views import LOGIN_URL, CACHE_TTL


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
