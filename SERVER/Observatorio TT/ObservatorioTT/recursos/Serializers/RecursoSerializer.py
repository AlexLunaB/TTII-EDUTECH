from rest_framework import serializers, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from taggit.models import Tag
from taggit_serializer.serializers import TaggitSerializer, TagListSerializerField

from recursos.models import Recurso, Categoria


class CategoriaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Categoria
    fields = ("__all__")

class RecursoReadSerializer(TaggitSerializer,serializers.ModelSerializer):
  categoria= CategoriaSerializer(many=True)
  tags = TagListSerializerField()

  class Meta:
    model = Recurso
    fields = ("__all__")
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







