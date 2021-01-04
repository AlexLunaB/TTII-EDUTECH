from rest_framework import serializers

from foroDiscusion.models import ForoDiscusion
from usuarios.serializers import UserSerializer, ProfileSerializer


class PostSerializer(serializers.ModelSerializer):

  administrador= serializers.HiddenField(default=serializers.CurrentUserDefault())

  class Meta:
    model =   ForoDiscusion
    fields = ("__all__")

class PostReadSerializer(serializers.ModelSerializer):

  administrador=UserSerializer()

  class Meta:
    model =   ForoDiscusion
    fields = ["temaDiscusion","descripcion","administrador","Imagen","created","id"]

class PostDetailSerializer(serializers.ModelSerializer):

  administrador=UserSerializer()

  class Meta:
    model =   ForoDiscusion
    fields = ["temaDiscusion","html","descripcion","administrador","Imagen","created","id"]



