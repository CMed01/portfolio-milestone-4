from django import forms
from .models import ContactRequest


class ContactForm(forms.ModelForm):
    """Creates Form from ContactRequest Modal"""
    class Meta:
        model = ContactRequest
        fields = ('name', 'email', 'message',)
        