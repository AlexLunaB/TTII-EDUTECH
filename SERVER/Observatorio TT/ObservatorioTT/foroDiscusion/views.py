from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from foroDiscusion.models import ForoDiscusion
from foroDiscusion.serializer import PostSerializer, PostReadSerializer, PostDetailSerializer


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
