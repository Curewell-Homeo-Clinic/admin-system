from django.urls import path, include
from .views import PatientsViewSet, DoctorsViewSet, AppointmentsViewSet, InvoicesViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'patients', PatientsViewSet)
router.register(r'doctors', DoctorsViewSet)
router.register(r'appointments', AppointmentsViewSet)
router.register(r'invoices', InvoicesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]