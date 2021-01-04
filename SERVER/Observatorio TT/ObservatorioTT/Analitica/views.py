from django.db.models import Count
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django_filters.views import FilterView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Analitica.filters.EstadoFilter import  RecursoFilter
from Analitica.serializers.RecursoEstadoSerializer import RecursoGraphSerializer
from ObservatorioTTApp.models import MexicoState
from recursos.models import Recurso
from collections import defaultdict, Counter
from taggit.models import Tag
import json

class  Index(TemplateView):
  template_name = "index.html"



class GraficasPorEstadoView(TemplateView):
  template_name = "reportes/porEstado.html"



@api_view(['GET'])
def  CantidadEdo(request):
  m=MexicoState.objects.annotate(Count('recurso')).order_by("-recurso__count")

  d=RecursoGraphSerializer(m,many=True)

  return Response(data=d.data)


@api_view(['GET'])
def GetTagsCommon( request):


  tag_frequency = defaultdict(int)
  for item in Recurso.objects.all():
    for tag in item.tags.all():
      tag_frequency[tag.name] += 1



  return Response(data=(tag_frequency), status=200)

class RecursoFilterView(FilterView):
    model = Recurso
    filterset_class = RecursoFilter
    template_name = 'reportes/NivelNacional.html'
