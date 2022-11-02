from django.db import models
from users.models import CustomUser
from collection.models import Post

class EdukasiComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commenter = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    
    content = models.TextField(max_length=255)

    upvotes = models.IntegerField()
    saved = models.IntegerField()