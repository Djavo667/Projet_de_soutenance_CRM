from django import forms

from .models import *

class ClientForm(forms.ModelForm):
    class Meta:
        model = client
        fields = ['nom', 'prenom', 'sexe', 'email', 'telephone']
    adresse = forms.CharField(label='Adresse', max_length=200)
    description = forms.CharField(label='Description', widget=forms.Textarea)