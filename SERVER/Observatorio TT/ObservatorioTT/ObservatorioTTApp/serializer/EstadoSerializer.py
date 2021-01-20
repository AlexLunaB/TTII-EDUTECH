from  rest_framework import serializers

from ObservatorioTTApp.models import MexicoState, MexicoMunicipio, IntitucionEmpresa


class EdoSerializer(serializers.ModelSerializer):
  class Meta:
    model =    MexicoState

    fields = ("__all__")
class MunicipioSerializer(serializers.ModelSerializer):
  class Meta:
    model =    MexicoMunicipio

    fields = ("__all__")

class InstitucionSerializer(serializers.ModelSerializer):
  class Meta:
    model =    IntitucionEmpresa

    fields = ("__all__")

