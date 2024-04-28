from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    """Creates Form from Profile Modal"""
    class Meta:
        model = Profile
        fields = ['bio', 'profile_image',]
