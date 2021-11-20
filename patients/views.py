from django.views.generic import ListView, DetailView
from .models import Patient
from django.shortcuts import redirect

def index(_request):
	response = redirect('/patients/')
	return response

class PatientList(ListView):
	model = Patient
	context_object_name = 'patients'

class PatientDetail(DetailView):
	model = Patient
	context_object_name = 'patient'
