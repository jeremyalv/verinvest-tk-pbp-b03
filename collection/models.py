from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    
    title = models.CharField(max_length=255)
    content = models.TextField()
    
    upvotes = models.IntegerField()
    viewers = models.IntegerField()
    comments_count = models.IntegerField()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    content = models.TextField()