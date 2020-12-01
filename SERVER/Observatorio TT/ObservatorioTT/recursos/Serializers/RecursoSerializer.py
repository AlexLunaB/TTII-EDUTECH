from rest_framework import serializers, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from recursos.models import Recurso, Categoria


class CategoriaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Categoria
    fields = ("__all__")

class RecursoReadSerializer(serializers.ModelSerializer):
  categoria= CategoriaSerializer(many=True)





  class Meta:
    model = Recurso
    fields = ("__all__")
class RecursoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Recurso
    fields = ("__all__")







