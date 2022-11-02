from django.db import models
from landing_page.models import CustomUser
from collection.models import Post

class EdukasiComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commenter = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    
    content = models.TextField()

    upvotes = models.IntegerField()