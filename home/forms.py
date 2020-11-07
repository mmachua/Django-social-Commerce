from django import forms
from home.models import Contact


class ContactForm(forms.ModelForm):
    phone  = forms.DecimalField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write your phone number here...'
        }
    ))
    class Meta:
        model = Contact

        fields = [
            'name',
            'email',
            'content'
            
        ]

