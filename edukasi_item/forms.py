from django import forms
from django.forms import ModelForm
from edukasi_item.models import EdukasiComment
from collection.models import Post

class EducationForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentForm(ModelForm):
    content= forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Write your comment here...'}))
    class Meta:
        model = EdukasiComment
        fields = ['content']
