from django.http import HttpResponse
from django.shortcuts import render

from .forms import ClientForm

#une liste des clients
data_clients = [ "client1", "client2", "client3", "client4", "client5" ]
# Create your views here.
def home_page(request):
    nbr_clients = len(data_clients)
    nom_boutique = "S_Cosmetique"
    return render(request, 'index.html', context={'nbr_clients': nbr_clients, 'nom_boutique': nom_boutique})

def list_clients(request):
    return render(request, "list_clients.html", context={'data_clients': data_clients})

def add_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            # data_clients.append(form.cleaned_data['nom'])4
            return HttpResponse("Client ajouté avec succès !")
    else:
        
        form = ClientForm()
        return render(request, "add_client.html", context={'form': form})
