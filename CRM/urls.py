
from django.contrib import admin
from django.urls import path, include
from LE_CRM import views
from LE_CRM.views import *

urlpatterns = [
    path('', home_page, name='index'),
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('list_clients/', liste_clients, name='liste_clients'),
    path('ajouter_client/', ajouter_client, name='ajouter_client'),
    path('list_produits/', liste_produits, name='liste_produits'),
    path('ajouter_produit/', ajouter_produit, name='ajouter_produit'),
    path('list_ventes/', liste_ventes, name='liste_ventes'),
    path('ajouter_vente/', ajouter_vente, name='ajouter_vente'),
    path('vente_status/<int:vente_id>/', changer_statut_vente, name='changer_statut_vente'),
    path('todo/', todo_list, name='todo_list'),
    path('ajouter_todo/', ajouter_todo, name='ajouter_todo'),
    path('todo/termine/<int:todo_id>/', marquer_todo_effectue, name='marquer_todo_effectue'),
    path('dashboard/', include('dashboard.urls')),
    path('admin/', admin.site.urls),
]
