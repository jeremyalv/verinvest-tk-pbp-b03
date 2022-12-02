from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_expert = models.BooleanField(default=False, null=True)
    first_name = models.CharField(max_length=20, default=None, null=True)
    last_name = models.CharField(max_length=20, default=None, null=True)
    email = models.EmailField(unique=True, default=None, null=True)
    birth_date = models.DateField(default=None, null=True)
    occupation = models.CharField(max_length=30, default=None, null=True)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.user.username
    

