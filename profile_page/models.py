from django.db import models
from landing_page.models import CustomUser
from collection.models import Post

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    
    birth_date = models.DateField()
    occupation = models.CharField(max_length=50)

