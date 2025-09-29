from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        related_name='patient_appointments',
        limit_choices_to={'user_type': 'patient', 'is_superuser': False, 'is_staff': False}
    )

    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='doctor_appointments',
        limit_choices_to={'user_type': 'doctor', 'is_superuser': False}
    )
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Only validate when both sides present
        if not self.patient_id or not self.doctor_id:
            return
        if self.patient_id == self.doctor_id:
            raise ValidationError("Patient and Doctor must be different users.")
        if getattr(self.patient, 'user_type', None) != 'patient':
            raise ValidationError("Selected patient must have user_type='patient'.")
        if getattr(self.doctor, 'user_type', None) != 'doctor':
            raise ValidationError("Selected doctor must have user_type='doctor'.")
        if self.patient.is_staff or self.patient.is_superuser:
            raise ValidationError("Patient cannot be staff or superuser.")
        if self.doctor.is_superuser:
            raise ValidationError("Doctor cannot be superuser.")

    def save(self, *args, **kwargs):
        self.full_clean()  # ensure validation also runs for programmatic creates
        return super().save(*args, **kwargs)

    def __str__(self):
        # return f"{self.patient.email} - {self.doctor.email} - {self.appointment_date}"
        return f"{self.patient.username} - {self.doctor.username} - {self.appointment_date}"