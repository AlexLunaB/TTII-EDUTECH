from rest_framework import serializers

from ObservatorioTTApp.models import MexicoState


class RecursoGraphSerializer(serializers.ModelSerializer):
  recurso__count = serializers.IntegerField(read_only=True,required=False)
  class Meta:
    model=MexicoState
    fields=["id","nombre","recurso__count"]


