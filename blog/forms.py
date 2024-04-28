from django import forms
from .models import PostComment


class BlogcommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('body',)
        