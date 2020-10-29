from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "ObservatorioTTApp/home.html")


def busqueda(request):
    return render(request, "ObservatorioTTApp/busqueda.html")


def perfil(request):
    return render(request, "ObservatorioTTApp/perfil.html")


def contacto(request):
    return render(request, "ObservatorioTTApp/contacto.html")


def acercaDe(request):
    return render(request, "ObservatorioTTApp/acercaDe.html")

