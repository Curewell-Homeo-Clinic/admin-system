from django.urls import path, include

from .views_file import (get_monthly_sales_chart_data,
                         get_daily_sales_chart_data)

from patients.views.dashboard import dashboard
from patients.views.patient import patient_detail, patient_list
from patients.views.doctor import doctor_detail, doctor_list
from patients.views.appointment import appointment_detail, appointment_list
from patients.views.invoice import invoice_detail, invoice_list, invoice_print
from patients.views.stats import stats

urlpatterns = [
    path('', dashboard, name='index'),
    path('patients/', patient_list, name='patients'),
    path('patient/<int:pk>/', patient_detail, name='patient'),
    path('appointments/', appointment_list, name="appointments"),
    path('appointment/<int:pk>/', appointment_detail, name="appointment"),
    path('doctors/', doctor_list, name='doctors'),
    path('doctor/<int:pk>/', doctor_detail, name='doctor'),
    path('invoices/', invoice_list, name='invoices'),
    path('invoice/<int:pk>/', invoice_detail, name='invoice'),
    path('invoice/<int:pk>/print/', invoice_print, name='invoice_print'),
    path('stats/', stats, name='stats'),
    path('api/v1/get_sales/<int:year>',
         get_monthly_sales_chart_data,
         name='api__get__monthly_sales'),
    path('api/v1/get_sales/<int:year>/<int:month>',
         get_daily_sales_chart_data,
         name='api__get__daily_sales'),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
    path('api/v1/', include('patients.api.urls')),
]