from django import forms
from cloudinary.models import CloudinaryField
from .models import Profile


class UpdateProfileForm(forms.ModelForm):
    """Creates Form from Profile Modal"""
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    class Meta:
        model = Profile
        fields = ['bio',]
