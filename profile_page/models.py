from django.db import models
from users.models import VerinvestUser
from collection.models import Post

class Profile(models.Model):
    user = models.OneToOneField(VerinvestUser, on_delete=models.CASCADE)
    
    avatar = models.FileField
    occupation = models.TextField(max_length=32)