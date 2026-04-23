from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count, Q
from django.utils import timezone
from datetime import timedelta
from LE_CRM.models import Vente, Client, Produit

@login_required
def dashboard_admin(request):
    if not request.user.groups.filter(name='admin').exists():
        return render(request, '403.html')  # Page d'erreur

    today = timezone.now().date()
    start_of_month = today.replace(day=1)
    start_of_year = today.replace(month=1, day=1)

    # Chiffre d'affaires
    ca_today = Vente.objects.filter(date_vente__date=today, statut='terminée').aggregate(Sum('total'))['total__sum'] or 0
    ca_month = Vente.objects.filter(date_vente__date__gte=start_of_month, statut='terminée').aggregate(Sum('total'))['total__sum'] or 0
    ca_year = Vente.objects.filter(date_vente__date__gte=start_of_year, statut='terminée').aggregate(Sum('total'))['total__sum'] or 0

    # Top clients
    top_clients = Client.objects.annotate(
        total_achats=Sum('vente__total', filter=Q(vente__statut='terminée'))
    ).order_by('-total_achats')[:5]

    # Top vendeurs
    top_vendeurs = Vente.objects.filter(statut='terminée').values('vendeur__username').annotate(
        total_ventes=Sum('total')
    ).order_by('-total_ventes')[:5]

    # Top produits
    top_produits = Produit.objects.annotate(
        total_vendu=Sum('vente__quantite', filter=Q(vente__statut='terminée'))
    ).order_by('-total_vendu')[:5]

    # Données pour graphiques (exemple simple)
    ventes_par_mois = Vente.objects.filter(statut='terminée', date_vente__year=today.year).extra(
        select={'month': 'strftime("%%m", date_vente)'}
    ).values('month').annotate(total=Sum('total')).order_by('month')

    context = {
        'ca_today': ca_today,
        'ca_month': ca_month,
        'ca_year': ca_year,
        'top_clients': top_clients,
        'top_vendeurs': top_vendeurs,
        'top_produits': top_produits,
        'ventes_par_mois': list(ventes_par_mois),
    }
    return render(request, 'dashboard/dashboard_admin.html', context)

@login_required
def dashboard_vendeur(request):
    if not request.user.groups.filter(name='vendeur').exists():
        return render(request, '403.html')

    today = timezone.now().date()
    start_of_month = today.replace(day=1)

    # Ventes personnelles
    ventes_today = Vente.objects.filter(vendeur=request.user, date_vente__date=today, statut='terminée')
    ca_perso_today = ventes_today.aggregate(Sum('total'))['total__sum'] or 0
    ca_perso_month = Vente.objects.filter(vendeur=request.user, date_vente__date__gte=start_of_month, statut='terminée').aggregate(Sum('total'))['total__sum'] or 0

    # Dernières transactions
    dernieres_ventes = Vente.objects.filter(vendeur=request.user, statut='terminée').order_by('-date_vente')[:10]

    context = {
        'ca_perso_today': ca_perso_today,
        'ca_perso_month': ca_perso_month,
        'dernieres_ventes': dernieres_ventes,
    }
    return render(request, 'dashboard/dashboard_vendeur.html', context)

@login_required
def dashboard_manager(request):
    if not request.user.groups.filter(name='manager').exists():
        return render(request, '403.html')

    today = timezone.now().date()
    start_of_month = today.replace(day=1)

    # Stats globales (moins détaillées)
    ca_month = Vente.objects.filter(date_vente__date__gte=start_of_month, statut='terminée').aggregate(Sum('total'))['total__sum'] or 0
    nbr_ventes_month = Vente.objects.filter(date_vente__date__gte=start_of_month, statut='terminée').count()

    # Performance vendeurs
    perf_vendeurs = Vente.objects.filter(statut='terminée', date_vente__date__gte=start_of_month).values('vendeur__username').annotate(
        total_ventes=Sum('total'),
        nbr_ventes=Count('id')
    ).order_by('-total_ventes')[:10]

    top_clients = Client.objects.annotate(
        total_achats=Sum('vente__total', filter=Q(vente__statut='terminée')),
        nbr_ventes=Count('vente__id', filter=Q(vente__statut='terminée'))
    ).filter(total_achats__gt=0).order_by('-total_achats')[:100]

    top_produit = Produit.objects.annotate(
        total_quantite=Sum('vente__quantite', filter=Q(vente__statut='terminée'))
    ).filter(total_quantite__gt=0).order_by('-total_quantite').first()

    context = {
        'ca_month': ca_month,
        'nbr_ventes_month': nbr_ventes_month,
        'perf_vendeurs': perf_vendeurs,
        'top_clients': top_clients,
        'top_produit': top_produit,
    }
    return render(request, 'dashboard/dashboard_manager.html', context)
