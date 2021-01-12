from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from foroDiscusion.models import ForoDiscusion
from foroDiscusion.serializer import PostSerializer, PostReadSerializer, PostDetailSerializer
from recursos.Serializers.RecursoSerializer import TagSerializer


class PostViewSet(
  mixins.ListModelMixin,
  mixins.UpdateModelMixin,
  mixins.CreateModelMixin,
  mixins.RetrieveModelMixin,
  mixins.DestroyModelMixin,
  viewsets.GenericViewSet):
  permission_classes = [IsAuthenticated]

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
    recurso=self.get_object()
    recomendacion=recurso.tags.similar_objects()[:5]
    R = PostReadSerializer(recomendacion, many=True, context={"request": request})
    return Response(data=R.data)




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
