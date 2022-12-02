from django.db import models
from django.contrib.auth.models import User

# class CustomUser(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     is_expert = models.BooleanField(default=False)
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     email = models.EmailField(unique=True)

#     USERNAME_FIELD = 'username'

#     def __str__(self):
#         return self.user.username
    
class Fortofolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=20)
    jumlah = models.IntegerField()
