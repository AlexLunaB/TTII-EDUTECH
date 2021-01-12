import django_filters
from django.db.models import Case, When
from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets, filters
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from taggit_serializer.serializers import TaggitSerializer

from ObservatorioTTApp.models import MexicoState
from ObservatorioTTApp.recomendador import Myrecommend
from recursos.Serializers.RecursoSerializer import RecursoSerializer, CategoriaSerializer, RecursoReadSerializer, \
  TagSerializer
from recursos.filters.filterRecursoView import RecursoFilter
from recursos.models import Recurso, Categoria, Rating
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

    return RecursoReadSerializer




  @action(detail=True,  methods=['get'])
  def recommend(self,request,pk):


    df = pd.DataFrame(list(Rating.objects.all().values()))
    nu = df.user_id.unique().shape[0]
    current_user_id = request.user.id

    # if new user not rated any movie
    if current_user_id > nu:
      movie = Recurso.objects.get(id=30)
      q = Rating(user=request.user, recurso=movie, rating=0)
      q.save()

    print("Current user id: ", current_user_id)
    prediction_matrix, Ymean = Myrecommend()
    my_predictions = prediction_matrix[:, current_user_id - 1] + Ymean.flatten()
    pred_idxs_sorted = np.argsort(my_predictions)
    pred_idxs_sorted[:] = pred_idxs_sorted[::-1]
    pred_idxs_sorted = pred_idxs_sorted + 1
    print(pred_idxs_sorted)
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(pred_idxs_sorted)])
    movie_list = list(Recurso.objects.filter(id__in=pred_idxs_sorted, ).order_by(preserved)[:10])
    R=RecursoSerializer(many=True,data=movie_list)
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

    return Response(data={"ok": 'ok'})

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







