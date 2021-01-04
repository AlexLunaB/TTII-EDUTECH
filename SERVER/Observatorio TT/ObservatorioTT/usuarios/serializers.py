from rest_framework import serializers

from usuarios.models import Usuario, Profile


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = Usuario
    fields = ("id","username")

class ProfileSerializer(serializers.ModelSerializer):
  usuario= UserSerializer
  class Meta:
    model = Profile
    fields = ("__all__")

