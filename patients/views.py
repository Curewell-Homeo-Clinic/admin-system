from patient_management_system.settings import CACHE_TTL
from .models import Patient
from django.shortcuts import redirect, render
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

def index(request):
	response = redirect('/patients/')
	return response

def get_patient(request, filter_patient = None):
	if filter_patient:
		print("DATA COMING FROM DB")
		patients = Patient.objects.filter(first_name__icontains=filter_patient)
	else:
		patients = Patient.objects.all()

	return patients

def patient_list(request):
	filter_patient = request.GET.get('filter_patient')
	if cache.get(filter_patient):
		patients = cache.get(filter_patient)
	else:
		if filter_patient:
			patients = get_patient(request, filter_patient)
			cache.set(filter_patient, patients)
		else:
			patients = get_patient(request)
	
	context = { 'patients': patients }
	return render(request, 'patients/patient_list.html', context=context)

def patient_detail(request, pk):
	if cache.get(pk):
		print("DATA COMING FROM CACHE")
		patient = cache.get(pk)
	else:
		print("DATA COMING FROM DB")
		patient = Patient.objects.get(pk=pk)
		cache.set(pk, patient)
	
	context = { 'patient': patient, 'patient_edit': f'/admin/patients/patient/{patient.id}/change', 'patient_delete': f'/admin/patients/patient/{patient.id}/delete' }
	return render(request, 'patients/patient_detail.html', context)