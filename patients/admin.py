from django.contrib import admin
from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age')
    list_display_links = ('id', 'name')
    list_filter = ('admitted_at', )
    
    def name(self, obj):
        if obj.last_name:
            return f'{ obj.first_name} { obj.last_name }'
        else:
            return obj.first_name