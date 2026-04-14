from django.contrib import admin
from .models import client, Catégorie, Produit, Vente, Todo

# Register your models here.
@admin.register(client)
class clientAdmin(admin.ModelAdmin):
    list_display = ("nom", "prenom", "sexe", "email", "telephone", "actif", "date_enregistrement")
    search_fields = ("nom", "prenom", "email", "telephone")
    list_filter = ("sexe", "actif", "date_enregistrement")
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

@admin.register(Catégorie)
class CatégorieAdmin(admin.ModelAdmin):
    list_display = ("nom", "description")
    search_fields = ("nom",)
    list_filter = ("nom",)

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ("nom", "marque", "catégorie", "prix", "stock", "stock_disponible")
    search_fields = ("nom", "marque")
    list_filter = ("catégorie", "marque")
    fieldsets = (
        ('Identité', {
            'fields': ('nom', 'marque', 'catégorie')
        }),
        ('Commercial', {
            'fields': ('prix', 'stock', 'actif'),
            'classes': ('wide',)
        }),
        ('Visuel', {
            'fields': ('image',),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('date_ajout',)

@admin.register(Vente)
class VenteAdmin(admin.ModelAdmin):
    list_display = ("client", "produit", "date_vente", "quantite", "total", "statut")
    search_fields = ("client__nom", "produit__nom")
    list_filter = ("date_vente", "statut")
    readonly_fields = ("date_vente", "total")


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ("client", "get_type_action_display", "date_action", "statut")
    search_fields = ("client__nom", "client__prenom", "description")
    list_filter = ("type_action", "statut", "date_action")
    ordering = ("-date_action",)