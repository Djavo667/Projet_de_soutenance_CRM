from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .forms import *
from .models import *

# Vue d'accueil du CRM
@login_required(login_url='connexion')
def home_page(request):
    nbr_clients = Client.objects.count()
    nom_boutique = "S_Cosmetique"
    context = {
        'nbr_clients': nbr_clients,
        'nom_boutique': nom_boutique,
    }
    return render(request, 'index.html', context=context)

# Créer vue liste_clients pour afficher tous les clients
@login_required(login_url='connexion')
def liste_clients(request):
    query = request.GET.get('q', '').strip()
    clients = Client.objects.all()
    if query:
        clients = clients.filter(telephone__icontains=query)
    return render(request, 'list_clients.html', context={'data_clients': clients, 'query': query})

# Créer vue ajouter_client avec ClientForm
@login_required(login_url='connexion')
def ajouter_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client ajouté avec succès.')
            return redirect('liste_clients')
        else:
            messages.error(request, 'Veuillez corriger les erreurs dans le formulaire.')
            # Debug: Afficher les erreurs du formulaire
            print("Erreurs du formulaire Client:", form.errors)
    else:
        form = ClientForm()
    return render(request, 'add_client.html', context={'form': form})

# Créer vue liste_produits pour afficher tous les produits
@login_required(login_url='connexion')
def liste_produits(request):
    query = request.GET.get('q', '').strip()
    produits = Produit.objects.all()
    if query:
        produits = produits.filter(
            Q(nom__icontains=query) |
            Q(marque__icontains=query) |
            Q(**{'catégorie__nom__icontains': query})
        )
    return render(request, 'list_produits.html', context={'produits': produits, 'query': query})

# Créer vue ajouter_produit avec ProduitForm
@login_required(login_url='connexion')
def ajouter_produit(request):
    # Assurer que les catégories par défaut existent
    Catégorie.creer_categories_parfum()
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produit ajouté avec succès.')
            return redirect('liste_produits')
        else:
            messages.error(request, 'Veuillez corriger les erreurs dans le formulaire.')
            # Debug: Afficher les erreurs du formulaire
            print("Erreurs du formulaire Produit:", form.errors)
    else:
        form = ProduitForm()
    return render(request, 'ajouter_produit.html', context={'form': form})

# Créer vue liste_ventes pour afficher toutes les ventes
@login_required(login_url='connexion')
def liste_ventes(request):
    ventes = Vente.objects.select_related('client', 'produit').all()
    return render(request, 'list_ventes.html', context={'ventes': ventes})

# Créer vue ajouter_vente avec VenteForm
@login_required(login_url='connexion')
def ajouter_vente(request):
    if request.method == 'POST':
        form = VenteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vente enregistrée avec succès.')
            return redirect('liste_ventes')
        else:
            messages.error(request, 'Veuillez corriger les erreurs dans le formulaire.')
            # Debug: Afficher les erreurs du formulaire
            print("Erreurs du formulaire Vente:", form.errors)
    else:
        form = VenteForm()
    return render(request, 'ajouter_vente.html', context={'form': form})

# Modifier le statut d'une vente existante
@login_required(login_url='connexion')
def changer_statut_vente(request, vente_id):
    vente = get_object_or_404(Vente, id=vente_id)
    if request.method == 'POST':
        statut = request.POST.get('statut')
        if statut in dict(Vente.statut_choix):
            vente.statut = statut
            vente.save()
    return redirect('liste_ventes')

# Liste des tâches à faire avec les clients
@login_required(login_url='connexion')
def todo_list(request):
    todos = Todo.objects.select_related('client').all()
    return render(request, 'todo_list.html', context={'todos': todos})

# Ajouter une tâche à la to-do list client
@login_required(login_url='connexion')
def ajouter_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tâche ajoutée avec succès.')
            return redirect('todo_list')
        else:
            messages.error(request, 'Veuillez corriger les erreurs dans le formulaire.')
            # Debug: Afficher les erreurs du formulaire
            print("Erreurs du formulaire Todo:", form.errors)
    else:
        form = TodoForm()
    return render(request, 'add_todo.html', context={'form': form})

# Marquer une tâche comme effectuée
@login_required(login_url='connexion')
def marquer_todo_effectue(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'POST':
        todo.statut = 'termine'
        todo.save()
    return redirect('todo_list')

@login_required(login_url='connexion')
def deconnexion(request):
    logout(request)
    return redirect('connexion')


def connexion(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Rediriger selon le groupe
            if user.groups.filter(name='admin').exists():
                return redirect('dashboard_admin')
            elif user.groups.filter(name='vendeur').exists():
                return redirect('dashboard_vendeur')
            elif user.groups.filter(name='manager').exists():
                return redirect('dashboard_manager')
            else:
                return redirect('index')  # Fallback
        else:
            error_message = "Nom d'utilisateur ou mot de passe incorrect."
            return render(request, 'connexion.html', context={'error_message': error_message})
    return render(request, 'connexion.html')
