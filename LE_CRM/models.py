from django.utils import timezone
from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Client(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nom")
    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    sexe = models.CharField(max_length=1, choices=[('M', 'Masculin'), ('F', 'Féminin')], verbose_name="Sexe")
    email = models.EmailField(verbose_name="Email")
    telephone = models.CharField(max_length=12, verbose_name="Téléphone")
    adresse = models.CharField(max_length=200, verbose_name="Adresse")
    description = models.TextField(default="vide", verbose_name="Description")
    date_enregistrement = models.DateTimeField(
        default=timezone.now, 
        verbose_name="Date d'enregistrement"
    )
    actif = models.BooleanField(default=True, verbose_name="Actif")

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
        ordering = ['prenom',"nom"]
        unique_together = ('telephone', 'email')
    def __str__(self):
        return f"{self.prenom} {self.nom}"
    

class Catégorie(models.Model):
    # Catégories de parfums
    CATEGORIES_PARFUM = [
        'parfum',
        'elixir',
        'eau de cologne',
        'eau de toilette',
        'eau de parfum',
        'extrait',
        'absolu',
        'eau fraiche',
    ]

    nom = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, max_length=200)

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"
        ordering = ['nom']

    def __str__(self):
        return self.nom

    @classmethod
    def creer_categories_parfum(cls):
        """Créer les catégories de parfum par défaut si elles n'existent pas."""
        for nom_categorie in cls.CATEGORIES_PARFUM:
            cls.objects.get_or_create(nom=nom_categorie)
    
class Produit(models.Model):
    # Produits (nom, catégorie, prix, description, etc.)
    nom = models.CharField(max_length=100, verbose_name="Nom du produit")
    marque = models.CharField(max_length=100, verbose_name="Marque")
    catégorie = models.ForeignKey(Catégorie, on_delete=models.CASCADE)
    prix = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    description = models.TextField(blank=True, verbose_name="Description")
    date_ajout = models.DateTimeField(default=timezone.now, verbose_name="Date d'ajout")
    stock = models.PositiveIntegerField(default=0, verbose_name="Stock disponible")
    image = models.ImageField(upload_to='produits/', blank=True, null=True, verbose_name="Image du produit")
    actif = models.BooleanField(default=True, verbose_name="Actif")

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"
        ordering = ['nom']

    def __str__(self):
        return f"{self.nom} - {self.marque}"

    def stock_status(self):
        if self.stock > 10:
            return "En stock"
        elif 1 <= self.stock <= 10:
            return "Stock faible"
        return "Rupture de stock"

    def stock_disponible(self):
        return self.stock > 0


Produit.stock_disponible.boolean = True

class Vente(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Client")
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, verbose_name="Produit")
    quantite = models.PositiveIntegerField(default=1, verbose_name="Quantité")
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], verbose_name="Prix unitaire")
    total = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], editable=False, verbose_name="Total de la vente")
    date_vente = models.DateTimeField(default=timezone.now, verbose_name="Date de vente")
    statut_choix = [
        ('en_cours', 'En cours'),
        ('terminée', 'Terminée'),
        ('annulée', 'Annulée'),
    ]
    statut = models.CharField(max_length=20, choices=statut_choix, default='en_cours', verbose_name="Statut")

    class Meta:
        verbose_name = "Vente"
        verbose_name_plural = "Ventes"
        ordering = ['-date_vente']

    def save(self, *args, **kwargs):
        self.total = self.quantite * self.prix_unitaire
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Vente de {self.produit} à {self.client} le {self.date_vente.strftime('%Y-%m-%d %H:%M:%S')}"


class Todo(models.Model):
    ACTION_CHOICES = [
        ('appel', 'Appel'),
        ('sms', 'SMS'),
        ('email', 'Email'),
        ('rendez_vous', 'Rendez-vous'),
    ]
    STATUT_CHOICES = [
        ('a_faire', 'À faire'),
        ('termine', 'Terminé'),
        ('annule', 'Annulé'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Client")
    type_action = models.CharField(max_length=20, choices=ACTION_CHOICES, verbose_name="Type d'action")
    date_action = models.DateTimeField(default=timezone.now, verbose_name="Date et heure")
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='a_faire', verbose_name="Statut")
    description = models.TextField(blank=True, verbose_name="Description")
    date_creation = models.DateTimeField(default=timezone.now, verbose_name="Date de création")

    class Meta:
        verbose_name = "Tâche"
        verbose_name_plural = "Tâches"
        ordering = ['-date_action']

    def __str__(self):
        return f"{self.get_type_action_display()} pour {self.client} le {self.date_action.strftime('%Y-%m-%d %H:%M')}"