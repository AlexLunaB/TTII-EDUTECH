from django.contrib.auth.models import User
from rest_framework import serializers, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from taggit.models import Tag
from taggit_serializer.serializers import TaggitSerializer, TagListSerializerField

from recursos.models import Recurso, Categoria, Rating, MyCustomTag, RecursosArchivo


class CategoriaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Categoria
    fields = ("__all__")


class RecursoArchivoSerializer(serializers.ModelSerializer):
  class Meta:
    model= RecursosArchivo
    fields=("__all__")

class RecursoReadSerializer(TaggitSerializer,serializers.ModelSerializer):
  tags = TagListSerializerField()
  calificacion= serializers.SerializerMethodField(read_only=True,required=False)
  recurso_img =RecursoArchivoSerializer(
                       many=True, read_only=True)


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
  image = serializers.ListField(required=False,
    child=serializers.FileField(max_length=100000,
                                allow_empty_file=False,
                                use_url=False) )



  def create(self, validated_data):

    print(validated_data)

    image = validated_data.get('image')
    if image:
      image=validated_data.pop('image')
    tags = validated_data.pop('tags')
    if tags:
      tags = map(lambda x: x.capitalize(), tags)
    instance = super(RecursoSerializer, self).create(validated_data)

    if image:
      for img in image:
        photo = RecursosArchivo.objects.create(archivo=img,recurso=instance,)
    instance.tags.set(*tags)
    return instance

  class Meta:
    model = Recurso
    fields = ("__all__")
class TagSerializer(serializers.ModelSerializer):
  class Meta:
    model = MyCustomTag
    fields = ("slug","name")







