from django.urls import path

from .views import (appointment_detail, appointment_list, dashboard,
                    doctor_detail, doctor_list, patient_list, patient_detail,
                    invoice_list, invoice_detail, invoice_print,
                    get_monthly_sales_chart_data, stats,
                    get_daily_sales_chart_data)

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
