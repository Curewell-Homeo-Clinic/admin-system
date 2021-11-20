from django.urls import path

from .views import index, patient_list, patient_detail

urlpatterns = [
	path('', index, name='index'),
    path('patients/', patient_list, name='patients'),
	path('patient/<int:pk>/', patient_detail, name='patient'),
]
