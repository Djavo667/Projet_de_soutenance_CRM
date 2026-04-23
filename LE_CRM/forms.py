from django import forms

from .models import *
from django.contrib.auth.forms import UserCreationForm

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nom', 'prenom', 'sexe', 'email', 'telephone', 'adresse', 'description']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du client'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom du client'}),
            'sexe': forms.Select(attrs={'class': 'form-select'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Adresse email'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresse complète'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description', 'rows': 3}),
        }

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'marque', 'catégorie', 'prix', 'description', 'stock', 'image', 'actif']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'marque': forms.TextInput(attrs={'class': 'form-control'}),
            'catégorie': forms.Select(attrs={'class': 'form-select'}),
            'prix': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'actif': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class VenteForm(forms.ModelForm):
    class Meta:
        model = Vente
        fields = ['client', 'produit', 'vendeur', 'quantite', 'prix_unitaire', 'statut', 'source']
        widgets = {
            'client': forms.Select(attrs={'class': 'form-select'}),
            'produit': forms.Select(attrs={'class': 'form-select'}),
            'vendeur': forms.Select(attrs={'class': 'form-select'}),
            'quantite': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'prix_unitaire': forms.NumberInput(attrs={'class': 'form-control'}),
            'statut': forms.Select(attrs={'class': 'form-select'}),
            'source': forms.Select(attrs={'class': 'form-select'}),
        }


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['client', 'type_action', 'date_action', 'statut', 'description']
        widgets = {
            'client': forms.Select(attrs={'class': 'form-select'}),
            'type_action': forms.Select(attrs={'class': 'form-select'}),
            'date_action': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'statut': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
    date_action = forms.DateTimeField(
        widget=forms.DateTimeInput(format='%Y-%m-%dT%H:%M', attrs={'type': 'datetime-local', 'class': 'form-control'}),
        input_formats=['%Y-%m-%dT%H:%M'],
        required=True,
        label='Date et heure',
    )   