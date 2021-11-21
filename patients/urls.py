from django.urls import path

from .views import appointment_detail, appointment_list, index, patient_list, patient_detail

urlpatterns = [
    path('', index, name='index'),
    path('patients/', patient_list, name='patients'),
    path('patient/<int:pk>/', patient_detail, name='patient'),
    path('appointments/', appointment_list, name="appointments"),
    path('appointment/<int:pk>/', appointment_detail, name="appointment"),
]
