from rest_framework import serializers
from taggit_serializer.serializers import TagListSerializerField

from ObservatorioTTApp.serializer.EstadoSerializer import InstitucionSerializer
from foroDiscusion.models import ForoDiscusion, ComentarioBlog
from usuarios.serializers import UserSerializer, ProfileSerializer, UserModelSerializer


class PostSerializer(serializers.ModelSerializer):

  administrador= serializers.HiddenField(default=serializers.CurrentUserDefault())
  tags = TagListSerializerField()

  def create(self, validated_data):
    print(validated_data)
    tags = validated_data.pop('tags')


    if tags:
      tags = map(lambda x: x.capitalize(), tags)
    instance = super().create(validated_data)
    instance.tags.set(*tags)
    return instance

  class Meta:
    model =   ForoDiscusion
    fields = ("__all__")

class PostReadSerializer(serializers.ModelSerializer):
  tags = TagListSerializerField()


  administrador=UserSerializer()


  class Meta:
    model =   ForoDiscusion
    fields = ["temaDiscusion","descripcion","administrador","Imagen","created","id","tags",]

class ComentarioBlogSerializer(serializers.ModelSerializer):
    usuario = UserModelSerializer()

    class Meta:
      model = ComentarioBlog
      fields = ("__all__")


class PostDetailSerializer(serializers.ModelSerializer):
  tags = TagListSerializerField()
  comentarioblog_set = ComentarioBlogSerializer(many=True,read_only=True,label="Comentarios")

  institucion= InstitucionSerializer()



  administrador=UserSerializer()

  class Meta:
    model =   ForoDiscusion
    fields = ["temaDiscusion","html","descripcion","administrador","Imagen","created","id","tags","comentarioblog_set","institucion","Archivo"]



