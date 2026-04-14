# CRM Parfum

CRM Parfum est un petit projet Django de gestion de clients, produits, ventes et tâches commerciales. Il permet de suivre des clients, d'enregistrer des produits et des ventes, et d'organiser une to-do list des actions commerciales (appels, SMS, emails, rendez-vous).

## Prérequis

- Python 3.11 ou 3.12
- Git
- Un terminal PowerShell ou Bash

## Installation

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
```

5. Appliquer les migrations :

```bash
python manage.py migrate
```

6. Lancer le serveur de développement :

```bash
python manage.py runserver
```

7. Ouvrir le navigateur :

```
http://127.0.0.1:8000/
```

## Structure du projet

```text
CRM Parfum/
├── CRM/                # Projet Django principal
│   ├── settings.py     # Configuration du projet
│   ├── urls.py         # Routes globales
│   ├── wsgi.py
│   ├── asgi.py
│   └── templates/      # Templates HTML partagés
├── LE_CRM/             # Application CRM
│   ├── models.py       # Modèles de données
│   ├── views.py        # Vues Django
│   ├── forms.py        # Formulaires Django
│   ├── admin.py        # Interface d'administration
│   └── migrations/     # Fichiers de migration de la base
├── db.sqlite3          # Base de données SQLite (doit être ignorée)
├── manage.py           # Script d'administration Django
├── requirements.txt    # Dépendances Python
├── .gitignore          # Fichiers exclus du dépôt
└── README.md           # Documentation du projet
```

## Fonctionnalités principales

- Gestion des clients
- Gestion des produits (parfums, catégories, prix, stock)
- Gestion des ventes avec statut
- To-do list commerciale pour appels, SMS, emails et rendez-vous
- Interface d'administration Django

## Points importants

- Le projet utilise SQLite par défaut.
- `CRM/settings.py` contient un `SECRET_KEY` hardcodé. Pour un usage en production, il faut externaliser ce secret dans une variable d'environnement.
- `DEBUG = True` est acceptable en développement, mais pas en production.

## Nettoyage du dépôt Git

Si `db.sqlite3` ou `media/` sont déjà suivis par Git, exécutez :

```bash
git rm --cached db.sqlite3
git rm --cached -r media
```

Si votre environnement virtuel est suivi, retirez-le aussi :

```bash
git rm --cached -r mon_env
```

Ensuite ajoutez les nouveaux fichiers et validez :

```bash
git add .gitignore requirements.txt README.md
git commit -m "Cleanup repository and add docs/configuration files"
git push
```

## Vérifications

- `git ls-files` montre que `db.sqlite3` et `media/produits/Dior_sauvage.jpg` étaient suivis. Ils doivent être retirés du dépôt.
- `python manage.py check` est passé avec succès.
- Les dépendances minimales réelles sont : `Django==6.0.4` et `Pillow==12.2.0`.

## Recommandations

- Ne pas committer `db.sqlite3` ni les fichiers `media/` générés.
- Ajouter un `.env` local pour les variables sensibles en production.
- Mettre à jour `ALLOWED_HOSTS` avant toute publication publique.
