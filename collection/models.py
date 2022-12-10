from django.db import models
from profile_page.models import Profile

class Post(models.Model):
    post_type = models.CharField(max_length=10)
    # author = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    author_username = models.CharField(max_length=150, null=True)
    date_created = models.DateField(auto_now_add=True)

    title = models.CharField(max_length=100)
    content = models.TextField()
    
    upvotes = models.IntegerField()
    viewers = models.IntegerField()
    comments_count = models.IntegerField()