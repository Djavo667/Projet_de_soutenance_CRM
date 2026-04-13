from django.http import HttpResponse
from django.shortcuts import render

from .forms import ClientForm
from .models import *

#une liste des clients
# data_clients = [ "client1", "client2", "client3", "client4", "client5" ]
# Create your views here.
def home_page(request):
    nbr_clients = len(client.objects.all())
    nom_boutique = "S_Cosmetique"
    context = {
        'nbr_clients': nbr_clients,
        'nom_boutique': nom_boutique
    }   
    return render(request, 'index.html', context=context)

def list_clients(request):
    return render(request, "list_clients.html", context={'data_clients': client.objects.all()})

def add_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save() # enregistre le client dans la base de données
            # data_clients.append(form.cleaned_data['nom'])4
            return HttpResponse("Client ajouté avec succès !")
    else:
        
        form = ClientForm()
        return render(request, "add_client.html", context={'form': form})
