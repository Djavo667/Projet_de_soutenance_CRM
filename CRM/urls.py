
from django.contrib import admin
from django.urls import path
from LE_CRM import views
from LE_CRM.views import *

urlpatterns = [
    path('', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('index/', home_page, name='home'),
    path('list_clients/', liste_clients, name='liste_clients'),
    path('add_client/', ajouter_client, name='ajouter_client'),
    path('list_produits/', liste_produits, name='liste_produits'),
    path('add_produit/', ajouter_produit, name='ajouter_produit'),
    path('list_ventes/', liste_ventes, name='liste_ventes'),
    path('add_vente/', ajouter_vente, name='ajouter_vente'),
    path('vente_status/<int:vente_id>/', changer_statut_vente, name='changer_statut_vente'),
    path('todo/', todo_list, name='todo_list'),
    path('add_todo/', ajouter_todo, name='ajouter_todo'),
    path('todo/termine/<int:todo_id>/', marquer_todo_effectue, name='marquer_todo_effectue'),
    path('tracking/', tracking, name='tracking'),
    path('admin/', admin.site.urls),
]
