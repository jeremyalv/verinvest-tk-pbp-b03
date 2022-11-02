from django.db import models
from django.contrib.auth.models import AbstractUser

class VerinvestUser(AbstractUser):
    class Meta:
        db_table = 'auth_user'
    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    email = models.EmailField(
        verbose_name='Email address',
        max_length=255,
        unique=True,
    )

    is_expert = models.BooleanField(default=False)

    birth_date = models.DateField()
    occupation = models.TextField(max_length=32)


        
