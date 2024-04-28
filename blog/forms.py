from django import forms
from .models import PostComment


class BlogcommentForm(forms.ModelForm):
    """Creates Form from PostComment Modal"""
    class Meta:
        model = PostComment
        fields = ('body',)
        