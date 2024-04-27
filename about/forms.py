from .models import ContactRequest
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ('name','email','message',)