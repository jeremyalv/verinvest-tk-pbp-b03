from enum import unique
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

class CustomUser(AbstractUser):    
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    is_expert = models.BooleanField(default=False)
    birth_date = models.DateField()
    occupation = models.TextField(max_length=32)

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'is_expert', 'birth_date', 'occupation']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    


        
