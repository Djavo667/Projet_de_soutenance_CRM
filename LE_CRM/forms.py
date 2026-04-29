from django import forms

from .models import *
from django.contrib.auth.forms import UserCreationForm

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nom', 'prenom', 'sexe', 'email', 'telephone', 'adresse', 'description']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du client (ex: Dupont)'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom du client (ex: Jean)'}),
            'sexe': forms.Select(attrs={'class': 'form-select'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Adresse email (ex: jean.dupont@email.com)'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone (ex: +223 70 00 00 00 avec indicatif)'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresse complète (ex: 123 Rue de la Paix, Bamako)'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description (optionnel)', 'rows': 3}),
        }

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'marque', 'catégorie', 'prix', 'description', 'stock', 'image', 'actif']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du produit (ex: Chanel No.5)'}),
            'marque': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Marque (ex: Chanel)'}),
            'catégorie': forms.Select(attrs={'class': 'form-select'}),
            'prix': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Prix en FCFA (ex: 150000.00)'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description du produit (optionnel)', 'rows': 3}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantité en stock (ex: 50)'}),
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
            'quantite': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'placeholder': 'Quantité (ex: 2)'}),
            'prix_unitaire': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Prix unitaire en FCFA (ex: 150000.00)'}),
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
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Description de la tâche (ex: Rappeler le client pour confirmation)'}),
        }
    date_action = forms.DateTimeField(
        widget=forms.DateTimeInput(format='%Y-%m-%dT%H:%M', attrs={'type': 'datetime-local', 'class': 'form-control'}),
        input_formats=['%Y-%m-%dT%H:%M'],
        required=True,
        label='Date et heure',
    )   