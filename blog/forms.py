from .models import PostComment
from django import forms

class BlogcommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('body',)