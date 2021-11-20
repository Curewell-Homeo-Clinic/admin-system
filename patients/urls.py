from django.urls import path

from .views import index, PatientDetail, PatientList

urlpatterns = [
	path('', index, name='index'),
    path('patients/', PatientList.as_view(), name='patients'),
	path('patient/<int:pk>/', PatientDetail.as_view(), name='patient'),
]
