from django import forms

class ClientForm(forms.Form):
    nom = forms.CharField(label='Nom', max_length=100)
    prenom = forms.CharField(label='Prénom', max_length=100)
    sexe = forms.ChoiceField(label='Sexe', choices=[('M', 'Masculin'), ('F', 'Féminin')])
    email = forms.EmailField(label='Email')
    telephone = forms.CharField(label='Téléphone', max_length=20)
    adresse = forms.CharField(label='Adresse', max_length=200)
    description = forms.CharField(label='Description', widget=forms.Textarea)