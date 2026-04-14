"""
URL configuration for CRM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from LE_CRM.views import (
    home_page,
    liste_clients,
    ajouter_client,
    liste_produits,
    ajouter_produit,
    liste_ventes,
    ajouter_vente,
    changer_statut_vente,
    todo_list,
    ajouter_todo,
    marquer_todo_effectue,
    tracking,
)

urlpatterns = [
    path('', home_page, name='home'),
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
