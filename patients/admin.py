from django.contrib import admin
from .models import Appointment, Doctor, Patient, Invoice


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age')
    list_display_links = ('name',)
    list_filter = ('admitted_at', )
    search_fields = ['first_name', 'last_name']

    def name(self, obj):
        if obj.last_name:
            return f'{ obj.first_name} { obj.last_name }'
        else:
            return obj.first_name


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_no', 'email', 'specialization')
    list_display_links = ('name',)
    search_fields = ['first_name', 'last_name']

    def name(self, obj):
        if obj.last_name:
            return f'{ obj.first_name} { obj.last_name }'
        else:
            return obj.first_name


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'date', 'time')
    list_display_links = ('id', 'patient')
    list_filter = (
        'date',
        'time',
        'doctor',
    )
    search_fields = ['patient__name', 'doctor__name']

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
	exclude = ['total_fee']
	list_display = ('id', 'patient', 'doctor', 'date', 'total_fee')
	list_display_links = ('id', 'patient', 'doctor')
	list_filter= ('date', 'doctor',)
	search_fields = ['patient__name', 'doctor__name']