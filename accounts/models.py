from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('client', 'Client'),
        ('freelancer', 'Freelancer'),
    )
    is_freelancer = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    bio = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True) 
    is_email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username
