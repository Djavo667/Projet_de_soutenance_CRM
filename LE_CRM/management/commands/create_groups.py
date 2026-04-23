from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'Créer les groupes de rôles pour le dashboard'

    def handle(self, *args, **options):
        Group.objects.get_or_create(name='admin')
        Group.objects.get_or_create(name='vendeur')
        Group.objects.get_or_create(name='manager')
        self.stdout.write(self.style.SUCCESS('Groupes créés avec succès'))