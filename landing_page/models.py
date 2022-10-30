from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    
