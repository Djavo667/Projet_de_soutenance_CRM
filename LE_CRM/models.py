from django.utils import timezone

from django.db import models

# Create your models here.
class client(models.Model):
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
