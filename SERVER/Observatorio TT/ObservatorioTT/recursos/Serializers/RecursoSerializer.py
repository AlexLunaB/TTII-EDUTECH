from django.contrib.auth.models import User
from rest_framework import serializers, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from taggit.models import Tag
from taggit_serializer.serializers import TaggitSerializer, TagListSerializerField

from recursos.models import Recurso, Categoria, Rating


class CategoriaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Categoria
    fields = ("__all__")

class RecursoReadSerializer(TaggitSerializer,serializers.ModelSerializer):
  categoria= CategoriaSerializer(many=True)
  tags = TagListSerializerField()
  calificacion= serializers.SerializerMethodField(read_only=True,required=False)

  class Meta:
    model = Recurso
    fields = ("__all__")


  def get_calificacion(self,obj):
    request= self.context.get("request",None)

    if not request.user.is_anonymous:
      try:
        user=request.user

        r=Rating.objects.get(user=user,recurso=obj)
        return r.rating
      except Rating.DoesNotExist:
        return None

class RecursoSerializer(serializers.ModelSerializer):
  tags = TagListSerializerField()

  def create(self, validated_data):
    tags = validated_data.pop('tags')
    instance = super(RecursoSerializer, self).create(validated_data)
    instance.tags.set(*tags)
    return instance

  class Meta:
    model = Recurso
    fields = ("__all__")
class TagSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tag
    fields = ("slug","name")







