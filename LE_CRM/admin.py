from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(client)
class clientAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste
    list_display = ("nom", "prenom", "sexe", "email", "telephone", "actif" , "date_enregistrement")
    # Filtres dans la barre latérale
    search_fields = ("nom", "prenom", "email", "telephone")
    # Filtre dans la barre latérale
    list_filter = ("sexe", "actif", "date_enregistrement")
    # Titres des sections
    fieldsets = (
        ('Informations principales', {
            'fields': ('nom', 'prenom', 'telephone')
        }),
        ('Contact', {
            'fields': ('email',),
            'classes': ('collapse',)
        }),
        ('Statut', {
            'fields': ('actif', 'date_enregistrement'),
            'classes': ('collapse',)
        }),
    )