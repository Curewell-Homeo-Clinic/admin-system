from .models import Patient
from django.shortcuts import redirect, render

def index(_request):
	response = redirect('/patients/')
	return response

def patient_list(request):
	patients = Patient.objects.all()
	return render(request, 'patients/patient_list.html', {'patients': patients})

def patient_detail(request, pk):
	patient = Patient.objects.get(pk=pk)
	return render(request, 'patients/patient_detail.html', {'patient': patient})