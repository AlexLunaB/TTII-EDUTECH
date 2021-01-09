import django_filters
from django_filters import FilterSet

from recursos.models import Recurso, MyCustomTag


class RecursoFilter(FilterSet):
  estado = django_filters.filters.BaseInFilter(
    field_name='estado',
  )

  municipio = django_filters.filters.BaseInFilter(
    field_name='municipio',
  )

  tags = django_filters.ModelMultipleChoiceFilter(
    field_name='tags__name',
    to_field_name='name',
    queryset=MyCustomTag.objects.all()
  )

  class Meta:
    model = Recurso
    fields = ['estado','municipio',"tags"]

