from django.urls import path

from ObservatorioTTApp import views

urlpatterns = [
   
    path('', views.home, name="Home"),
    path('busqueda', views.busqueda, name="Busqueda"),
    path('perfil', views.perfil, name="Perfil"),
    path('contacto', views.contacto, name="Contacto"),
    path('acercaDe', views.acercaDe, name="AcercaDe"),
]