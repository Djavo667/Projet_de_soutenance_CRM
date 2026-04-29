# CRM Parfum

CRM Parfum est un projet Django complet pour gérer un CRM de parfumerie. Ce CRM permet de gérer les clients, les produits, les ventes et les actions commerciales dans une interface simple avec des tableaux de bord et une authentification basée sur des groupes.

## Présentation du projet

Le projet est construit autour de deux applications principales :

- `CRM/` : le projet Django principal avec la configuration globale et les templates communs.
- `LE_CRM/` : l'application métier qui contient les modèles, les formulaires, les vues et les routes pour le CRM.
- `dashboard/` : l'application contenant des dashboards spécifiques pour les groupes `admin`, `vendeur` et `manager`.

### Objectif

Créer un CRM simple et fonctionnel pour une parfumerie, capable de :

- Gérer les clients et leurs informations de contact.
- Structurer les produits par catégorie, marque et stock.
- Enregistrer des ventes avec calcul automatique du total et ajustement du stock.
- Proposer une to-do list commerciale pour suivre les actions à réaliser.
- Offrir des dashboards adaptés aux rôles utilisateurs.
- Rechercher des clients et des produits facilement.

## Architecture du projet

### Modèles

`LE_CRM/models.py` contient :

- `Client` : nom, prénom, sexe, email, téléphone, adresse, description, statut actif.
- `Catégorie` : catégories de parfums avec création automatique de valeurs par défaut.
- `Produit` : nom, marque, catégorie, prix, description, stock, image, actif.
- `Vente` : client, produit, vendeur (utilisateur Django), quantité, prix unitaire, total, date, source, statut, ajustement du stock.
- `Todo` : tâches commerciales liées à un client, type d'action, date, statut et description.
- `Utilisateur` : modèle additionnel non utilisé pour l'authentification Django standard.

### Formulaires

`LE_CRM/forms.py` utilise des `ModelForm` pour créer des formulaires Bootstrap-friendly pour :

- création de clients
- création de produits
- création de ventes
- création de tâches

Les widgets sont personnalisés pour afficher des champs proprement dans les templates.

### Vues

`LE_CRM/views.py` gère :

- l’affichage des listes de clients, produits, ventes et tâches.
- l’ajout de clients, produits, ventes et tâches.
- la recherche de clients par téléphone et de produits par nom/marque/catégorie.
- le passage des ventes terminées et l'ajustement automatique du stock.
- l’authentification et la déconnexion.

`dashboard/views.py` gère :

- `dashboard_admin` : statistiques globales, top clients, top vendeurs, top produits, CA journalier/mois/année.
- `dashboard_vendeur` : CA personnel du jour et du mois, dernières ventes.
- `dashboard_manager` : CA du mois, nombre de ventes, top 100 clients, top produit vendu, performance des vendeurs.

### Templates

Les templates utilisent Bootstrap 5 via CDN et sont organisés ainsi :

- `CRM/templates/base.html` : layout principal, barre de navigation et footer.
- `CRM/templates/dashboard_base.html` : layout dashboard avec sidebar.
- `CRM/templates/list_clients.html` : liste clients avec barre de recherche par téléphone.
- `CRM/templates/list_produits.html` : liste produits avec barre de recherche par nom/marque/catégorie.
- `CRM/templates/add_todo.html` : formulaire de tâche commerciale.
- `CRM/templates/dashboard/*.html` : dashboards selon les rôles.

### Routes principales

`CRM/urls.py` expose :

- `/` → page d'accueil
- `/connexion/` → page de connexion
- `/deconnexion/` → déconnexion
- `/list_clients/` → liste des clients
- `/ajouter_client/` → ajout d’un client
- `/list_produits/` → liste des produits
- `/ajouter_produit/` → ajout d’un produit
- `/list_ventes/` → liste des ventes
- `/ajouter_vente/` → ajout d’une vente
- `/vente_status/<int:vente_id>/` → changer le statut d’une vente
- `/todo/` → liste des tâches
- `/ajouter_todo/` → ajout d'une tâche
- `/todo/termine/<int:todo_id>/` → marquer une tâche terminée
- `/dashboard/` → inclut les dashboards par rôle

Dashboard :

- `/dashboard/admin/`
- `/dashboard/vendeur/`
- `/dashboard/manager/`

## Installation pas-à-pas

Le projet est désormais conçu pour fonctionner avec une base de données MySQL/MariaDB. Avant d’appliquer les migrations, vérifiez que votre serveur MySQL est accessible et que la section `DATABASES` de `CRM/settings.py` est configurée avec vos identifiants.

1. Cloner le dépôt :

```bash
git clone <URL_DU_REPO>
cd "CRM Parfum"
```

2. Créer un environnement virtuel :

```bash
python -m venv mon_env
```

3. Activer l'environnement :

- PowerShell :

```powershell
& "${PWD}\mon_env\Scripts\Activate.ps1"
```

- Bash :

```bash
source mon_env/bin/activate
```

4. Installer les dépendances :

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install mysqlclient
```

5. Créer la base de données MySQL :

```sql
CREATE DATABASE gp CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

6. Mettre à jour `CRM/settings.py` pour utiliser MySQL :

- `ENGINE`: `django.db.backends.mysql`
- `NAME`: nom de la base (par défaut `gp`)
- `USER`, `PASSWORD`, `HOST`, `PORT`
- éventuellement `OPTIONS`: `init_command` avec `STRICT_TRANS_TABLES`

7. Appliquer les migrations :

```bash
python manage.py migrate
```

8. Créer un superutilisateur si nécessaire :

```bash
python manage.py createsuperuser
```

9. Lancer le serveur de développement :

```bash
python manage.py runserver
```

10. Ouvrir l’application :

```text
http://127.0.0.1:8000/
```

## Comment le projet a été construit

1. Création du projet Django et de l’application métier `LE_CRM`.
2. Définition des modèles principaux : clients, catégories, produits, ventes et tâches.
3. Ajout de la logique de calcul automatique du total de vente et de l’ajustement du stock dans `Vente.save()`.
4. Mise en place d’un formulaire Django pour chaque modèle en utilisant `ModelForm`.
5. Création de vues pour afficher, ajouter et filtrer les données.
6. Intégration de l’authentification Django et redirection selon le groupe de l’utilisateur.
7. Construction de dashboards spécifiques pour les rôles `admin`, `vendeur` et `manager`.
8. Ajout d’une interface Bootstrap 5 dans les templates pour un rendu propre et responsive.
9. Ajout de fonctions de recherche dans les listes clients et produits.
10. Nettoyage du projet : suppression des anciennes vues de tracking et amélioration de l’UX.

## Bonnes pratiques et remarques

- Ne jamais exposer `SECRET_KEY` et `DEBUG=True` en production.
- Pour un projet réel, limiter `ALLOWED_HOSTS`.
- Ne pas stocker les identifiants MySQL dans le dépôt : utilisez un fichier `.env` ou des variables d’environnement.
- Ajouter les fichiers media au `.gitignore`.
- Tester les scripts avec `python manage.py check` et `python manage.py makemigrations` avant tout commit.

## Améliorations possibles

- Ajouter des permissions fines par groupe et par action.
- Améliorer la lisibilité des tableaux avec pagination.
- Ajouter des graphiques JavaScript dans le dashboard.
- Permettre l’upload d’images produit avec une gestion plus robuste du média.
- Mettre en place un système de notifications pour les tâches à venir.

## Vérification rapide

```bash
python manage.py check
python manage.py migrate
python manage.py runserver
```

Ensuite, connectez-vous et utilisez les dashboards par rôle pour vérifier :

- l’affichage des clients et la recherche par téléphone,
- l’affichage des produits et la recherche par marque/nom/catégorie,
- l’ajout de ventes et l’ajustement du stock,
- le top produit vendu et les 100 meilleurs clients sur le dashboard manager.
