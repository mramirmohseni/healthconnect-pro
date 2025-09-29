from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPE_CHOICES = [
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    ]
    user_type = models.CharField(max_length=10,
        choices=USER_TYPE_CHOICES, 
        default='patient'
    )
    
    def __str__(self):
        return self.get_full_name() or self.username or self.email or f'User {self.pk}'
    