from django.db import migrations


def create_default_categories(apps, schema_editor):
    Catégorie = apps.get_model('LE_CRM', 'Catégorie')
    categories = [
        'parfum',
        'elixir',
        'eau de cologne',
        'eau de toilette',
        'eau de parfum',
        'extrait',
        'absolu',
        'eau fraiche',
    ]
    for nom in categories:
        Catégorie.objects.get_or_create(nom=nom)


def reverse_default_categories(apps, schema_editor):
    Catégorie = apps.get_model('LE_CRM', 'Catégorie')
    noms = [
        'parfum',
        'elixir',
        'eau de cologne',
        'eau de toilette',
        'eau de parfum',
        'extrait',
        'absolu',
        'eau fraiche',
    ]
    Catégorie.objects.filter(nom__in=noms).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('LE_CRM', '0004_produit_actif_vente'),
    ]

    operations = [
        migrations.RunPython(create_default_categories, reverse_default_categories),
    ]
