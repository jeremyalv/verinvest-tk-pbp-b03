from django.db import models
from users.models import CustomUser
from collection.models import Post

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    
    avatar = models.FileField
    occupation = models.TextField(max_length=32)