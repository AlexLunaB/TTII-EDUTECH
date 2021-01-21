from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets, filters
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from foroDiscusion.models import ForoDiscusion, ComentarioBlog
from foroDiscusion.serializer import PostSerializer, PostReadSerializer, PostDetailSerializer, ComentarioBlogSerializer
from recursos.Serializers.RecursoSerializer import TagSerializer


class PostViewSet(
  mixins.ListModelMixin,
  mixins.UpdateModelMixin,
  mixins.CreateModelMixin,
  mixins.RetrieveModelMixin,
  mixins.DestroyModelMixin,
  viewsets.GenericViewSet):
  permission_classes = [IsAuthenticated]

  filter_backends = (filters.OrderingFilter, filters.SearchFilter)
  search_fields = ['descripcion', 'temaDiscusion', "tags__name"]

  def get_serializer_class(self):
    """Return serializer based on action."""
    if self.action == 'create':
      return PostSerializer
    if self.action == 'update':
      return PostSerializer
    if self.action == 'retrieve':

      return  PostDetailSerializer
    else:
      return PostReadSerializer


  @action(detail=False, methods=['get'])
  def Tags(self,request):



    tags=ForoDiscusion.tags.all()
    print(tags)
    ts=TagSerializer(data=tags,many=True)
    print(ts.is_valid())
    print(ts.errors)


    return Response(ts.data)

  @action(detail=True, methods=["Get"])
  def Similares(self, request,pk):
    foro=self.get_object()
    recomendacion=foro.tags.similar_objects()[:5]
    R = PostReadSerializer(recomendacion, many=True, context={"request": request})
    return Response(data=R.data)



  @action(detail=False, methods=["Get"])
  def PorUsuario(self, request,):
    usuario=self.request.user
    ob = usuario.forodiscusion_set.all()
    R = PostReadSerializer(ob, many=True, context={"request": request})
    return Response(data=R.data)

  @action(detail=True, methods=["POST"])
  def Comentar(self, request, pk):

    self.get_object()

    usuario = self.request.user
    Comenta = request.data.get("comentario")
    if not Comenta:
      return Response(data={"Comentario": ''}, status=400)

    if usuario.is_anonymous:
      return Response(data={"error": 'Usuario No logueado'}, status=400)
    recurso = self.get_object()
    c = ComentarioBlog.objects.create(comentario=Comenta, usuario=usuario, recurso=recurso)
    cs = ComentarioBlogSerializer(c)
    return Response(data=cs.data, status=400)




  def perform_create(self, serializer):
    serializer=serializer.save(administrador=self.request.user)
    a= super().perform_create(serializer)
    return a

  def create(self, request, *args, **kwargs):
    print(self.request.POST)
    print(self.request.data)
    return super().create(request, *args, **kwargs)



  queryset = ForoDiscusion.objects.all()
  serializer_class = PostSerializer
