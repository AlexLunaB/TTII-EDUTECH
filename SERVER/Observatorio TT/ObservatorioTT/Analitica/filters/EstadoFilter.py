import django_filters
from django_filters.widgets import RangeWidget

from ObservatorioTTApp.models import MexicoState
from recursos.models import Recurso


class RecursoFilter(django_filters.FilterSet):
  fechaCreacion = django_filters.DateFromToRangeFilter(field_name="fechaCreacion", widget=RangeWidget(attrs={'type': 'date'}),
                                               label="Rango de fecha")




  Estado = django_filters.filters.ModelChoiceFilter(
    field_name='estado',
    label="Estado",
    queryset=MexicoState.objects.all()
  )

  class Meta:
    model = Recurso
    fields = ['Estado','fechaCreacion']
