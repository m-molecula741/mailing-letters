from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """форма подписки по email"""
    class Meta:
        model = Contact
        fields = '__all__'