from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Appointment

# Register your models here.
User = get_user_model()

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'appointment_date', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('patient__username', 'patient__email', 'doctor__username', 'doctor__email')
    date_hierarchy = 'appointment_date'
    ordering = ('-appointment_date',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'patient':
            kwargs['queryset'] = User.objects.filter(user_type='patient', is_superuser=False, is_staff=False)
        elif db_field.name == 'doctor':
            kwargs['queryset'] = User.objects.filter(user_type='doctor')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)