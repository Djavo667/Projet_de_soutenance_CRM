from django.shortcuts import render, redirect

from .forms import ClientForm, ProduitForm, VenteForm
from .models import client, Produit, Vente

# Vue d'accueil du CRM
def home_page(request):
    nbr_clients = client.objects.count()
    nom_boutique = "S_Cosmetique"
    context = {
        'nbr_clients': nbr_clients,
        'nom_boutique': nom_boutique,
    }
    return render(request, 'index.html', context=context)

# Créer vue liste_clients pour afficher tous les clients
def liste_clients(request):
    clients = client.objects.all()
    return render(request, 'list_clients.html', context={'data_clients': clients})

# Créer vue ajouter_client avec ClientForm
def ajouter_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_clients')
    else:
        form = ClientForm()
    return render(request, 'add_client.html', context={'form': form})

# Créer vue liste_produits pour afficher tous les produits
def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'list_produits.html', context={'produits': produits})

# Créer vue ajouter_produit avec ProduitForm
def ajouter_produit(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('liste_produits')
    else:
        form = ProduitForm()
    return render(request, 'ajouter_produit.html', context={'form': form})

# Créer vue liste_ventes pour afficher toutes les ventes
def liste_ventes(request):
    ventes = Vente.objects.select_related('client', 'produit').all()
    return render(request, 'list_ventes.html', context={'ventes': ventes})

# Créer vue ajouter_vente avec VenteForm
def ajouter_vente(request):
    if request.method == 'POST':
        form = VenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_ventes')
    else:
        form = VenteForm()
    return render(request, 'ajouter_vente.html', context={'form': form})

# Recherche d'un client par téléphone
def tracking(request):
    message = ''
    client_trouve = None
    if request.method == 'POST':
        num_client = request.POST.get('num_client', '').strip()
        try:
            client_trouve = client.objects.get(telephone=num_client)
            message = f"Client trouvé : {client_trouve}"
        except client.DoesNotExist:
            message = "Aucun client trouvé avec ce numéro."
    return render(request, 'tracking.html', context={'message': message, 'client_trouve': client_trouve})