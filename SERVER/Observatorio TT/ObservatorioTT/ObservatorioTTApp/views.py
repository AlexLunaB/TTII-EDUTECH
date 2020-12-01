from django.shortcuts import render, HttpResponse

# Create your views here.
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ObservatorioTTApp.models import MexicoState
from ObservatorioTTApp.serializer.EstadoSerializer import EdoSerializer, MunicipioSerializer


class EstadosMexicoViewSet(
  mixins.ListModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):




    queryset = MexicoState.objects.all()
    serializer_class = EdoSerializer

    @action(detail=True, methods=['get'])
    def GetMunicipio(self, request, pk=None):
      a=self.get_object()

      municipios=a.mexicomunicipio_set.all()
      m=MunicipioSerializer(municipios,many=True)

      return Response(data=m.data,status=200)




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

