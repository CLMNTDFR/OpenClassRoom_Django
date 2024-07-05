from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    ROLE_CHOICES = (
        (CREATOR, 'Creator'),
        (SUBSCRIBER, 'Subscriber'),
    )
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Role')
