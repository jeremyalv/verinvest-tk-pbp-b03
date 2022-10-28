from django import forms

class ForumForm(forms.Form):
    # Add form code here
    title = forms.CharField(max_length=255)
    content = forms.CharField(widget=forms.Textarea)