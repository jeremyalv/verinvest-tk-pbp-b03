from django.db import models
from django.contrib.auth.models import User
from collection.models import Post

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    avatar = models.FileField
    occupation = models.TextField(max_length=32)