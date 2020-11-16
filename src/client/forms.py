from django import forms
from .models import Client
from phonenumber_field.formfields import PhoneNumberField

class ClientForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        password = forms.CharField(widget=forms.PasswordInput)
        tel = PhoneNumberField()
        model = Client
        fields = ['nom','prenom','email','tel','password']
