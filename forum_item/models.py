from django.db import models
from users.models import VerinvestUser
from collection.models import Post

class ForumComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commenter = models.ForeignKey(VerinvestUser, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)

    content = models.TextField(max_length=255)

    upvotes = models.IntegerField()
    saved = models.IntegerField()
    comments_count = models.IntegerField()

class ForumOpvote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    upvoter = models.ForeignKey(VerinvestUser, on_delete=models.CASCADE)