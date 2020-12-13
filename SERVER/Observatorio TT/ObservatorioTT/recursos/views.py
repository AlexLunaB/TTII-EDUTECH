from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from taggit_serializer.serializers import TaggitSerializer

from ObservatorioTTApp.models import MexicoState
from recursos.Serializers.RecursoSerializer import RecursoSerializer, CategoriaSerializer, RecursoReadSerializer, \
  TagSerializer
from recursos.models import Recurso, Categoria


class RecursoViewSet(mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
  queryset = Recurso.objects.all()
  serializer_class = RecursoSerializer

  def get_serializer_class(self):
    """Return serializer based on action."""
    if self.action == 'create':
      return RecursoSerializer
    if self.action == 'update':
      return RecursoSerializer

    return RecursoReadSerializer

  @action(detail=False, methods=['get'])
  def Tags(self,request):



    tags=Recurso.tags.all()
    print(tags)
    ts=TagSerializer(data=tags,many=True)
    print(ts.is_valid())
    print(ts.errors)


    return Response(ts.data)




  @action(detail=False, methods=['get'])
  def Estado(self, request, pk=None):
    print(request.data)



    estado=self.request.query_params.get("Estado")
    print(estado)


    if estado:
      ob=get_object_or_404(MexicoState,pk=estado)

      ob=ob.recurso_set.all()


      R=RecursoSerializer(ob,many=True)
      return Response(data=R.data)




    else:
      return  Response(status=404)


class CategoriaViewSet(mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
  queryset = Categoria.objects.all()
  serializer_class = CategoriaSerializer
