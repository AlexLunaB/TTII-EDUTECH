from rest_framework import serializers
from taggit_serializer.serializers import TagListSerializerField

from foroDiscusion.models import ForoDiscusion
from usuarios.serializers import UserSerializer, ProfileSerializer


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
    fields = ["temaDiscusion","descripcion","administrador","Imagen","created","id","tags"]




class PostDetailSerializer(serializers.ModelSerializer):
  tags = TagListSerializerField()


  administrador=UserSerializer()

  class Meta:
    model =   ForoDiscusion
    fields = ["temaDiscusion","html","descripcion","administrador","Imagen","created","id","tags"]



