from django.forms import ModelForm
from edukasi_item.models import EdukasiComment
from collection.models import Post

class EducationForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentForm(ModelForm):
    class Meta:
        model = EdukasiComment
        fields = ['content']