import json

import django_filters
from django.db.models import Case, When
from django.shortcuts import render

# Create your views here.
from numpy import load
from rest_framework import mixins, viewsets, filters
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from taggit_serializer.serializers import TaggitSerializer

from ObservatorioTT import settings
from ObservatorioTTApp.models import MexicoState
from ObservatorioTTApp.recomendador import Myrecommend
from recursos.Serializers.RecursoSerializer import RecursoSerializer, CategoriaSerializer, RecursoReadSerializer, \
  TagSerializer, ComentarioSerializer, RecursoDetailSerializer
from recursos.filters.filterRecursoView import RecursoFilter
from recursos.models import Recurso, Categoria, Rating, Comentario
from rest_framework.permissions import IsAuthenticated
import  numpy as np
import pandas as pd



class RecursoViewSet(mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
  queryset = Recurso.objects.all()
  serializer_class = RecursoSerializer
  filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
  filterset_class = RecursoFilter

  search_fields = ['descripcion','nombreRecurso',"tags__name"]

  def get_serializer_class(self):
    """Return serializer based on action."""
    if self.action == 'create':
      return RecursoSerializer
    if self.action == 'update':
      return RecursoSerializer
    if self.action == 'retrieve':
      return RecursoDetailSerializer

    return RecursoReadSerializer

  def list(self, request, *args, **kwargs):
    """Add circle to serializer context."""
    response = super().list(request, *args, **kwargs)

    recursos=super(RecursoViewSet, self).filter_queryset(self.queryset)
    recurso_estado={}
    for recurso in recursos:
      if not recurso.estado.id in recurso_estado:
        recurso_estado[recurso.estado.id] = {"conteo": 0, "id": recurso.estado.id}
      recurso_estado[recurso.estado.id]["conteo"] += 1

    data = {
      'recursos': response.data,
      'conteo': recurso_estado
    }
    response.data = data
    return response







  @action(detail=False,  methods=['get'])
  def recommend(self,request):



    df = pd.DataFrame(list(Rating.objects.all().values()))
    nu = df.user_id.unique().shape[0]
    current_user_id = int(request.user.id)
    # if new user not rated any movie
    if not Rating.objects.filter(user=request.user).exists():
      movie = Recurso.objects.get(id=30)
      q = Rating(user=request.user, recurso=movie, rating=0)
      q.save()

    print("Current user id: ", current_user_id)
    prediction_matrix=load(str(settings.BASE_DIR)+'/ma.npy')
    Ymean=load(str(settings.BASE_DIR)+'/mb.npy')
    my_predictions = prediction_matrix[:, current_user_id - 1] + Ymean.flatten()
    pred_idxs_sorted = np.argsort(my_predictions)
    pred_idxs_sorted[:] = pred_idxs_sorted[::-1]
    pred_idxs_sorted = pred_idxs_sorted + 1
    print(pred_idxs_sorted)
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(pred_idxs_sorted)])
    movie_list = list(Recurso.objects.filter(id__in=pred_idxs_sorted, ).order_by(preserved)[:10])
    R=RecursoReadSerializer(many=True,data=movie_list, context={"request":request})
    R.is_valid()



    return  Response(data={'recursos_list': R.data})


  def perform_create(self, serializer):
    serializer=serializer.save(Usuario=self.request.user)
    a= super().perform_create(serializer)
    return a





  @action(detail=False, methods=['get'])
  def Tags(self,request):
    tags=Recurso.tags.all()
    print(tags)
    ts=TagSerializer(data=tags,many=True)
    print(ts.is_valid())
    print(ts.errors)
    return Response(ts.data)



  @action(detail=False, methods=["Get"])
  def PorUsuario(self, request,):
    usuario=self.request.user
    ob = usuario.recurso_set.all()
    R = RecursoReadSerializer(ob, many=True, context={"request": request})
    return Response(data=R.data)

  @action(detail=True, methods=["POST"])
  def CalificaRecurso(self, request,pk):
    print(request.data.get("calificacion"))



    usuario=self.request.user
    calificacion=request.data.get("calificacion")

    if not  calificacion:
      return Response(data={"error":'calificacion no proporcionada'})


    recurso=self.get_object()
    source, created  =Rating.objects.get_or_create(recurso=recurso, user=usuario,)
    print(source)
    source.rating=  calificacion

    source.save()

    return Response(data={"ok": 'ok'})\

  @action(detail=True, methods=["POST"])
  def Comentar(self, request,pk):


    self.get_object()

    usuario=self.request.user
    Comenta=request.data.get("comentario")
    if not Comenta:
      return Response(data={"Comentario": ''}, status=400)

    if  usuario.is_anonymous:
      return Response(data={"error":'Usuario No logueado'},status=400)
    recurso=self.get_object()
    c=Comentario.objects.create(comentario=Comenta,usuario=usuario,recurso=recurso)
    cs=ComentarioSerializer(c)
    return Response(data=cs.data,status=400)

  @action(detail=True, methods=["Get"])
  def Similares(self, request,pk):
    recurso=self.get_object()

    recomendacion=recurso.tags.similar_objects()[:5]
    R = RecursoReadSerializer(recomendacion, many=True, context={"request": request})
    return Response(data=R.data)



    return Response(data={"ok": 'ok'})




  def get_permissions(self):
    if self.action == 'CalificaRecurso':
      return [IsAuthenticated()]
    else:
      return super().get_permissions()

  @action(detail=False, methods=['get'])
  def Estado(self, request, pk=None):
    print(request.data)



    estado=self.request.query_params.get("Estado")
    print(estado)


    if estado:
      ob=get_object_or_404(MexicoState,pk=estado)

      ob=ob.recurso_set.all()


      R=RecursoReadSerializer(ob,many=True, context={"request":request})
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





