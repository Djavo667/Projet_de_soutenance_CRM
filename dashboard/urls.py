from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.dashboard_admin, name='dashboard_admin'),
    path('vendeur/', views.dashboard_vendeur, name='dashboard_vendeur'),
    path('manager/', views.dashboard_manager, name='dashboard_manager'),
]