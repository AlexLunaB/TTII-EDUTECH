from django.conf import settings
from django.urls import path, include
from django.views import static

from Analitica.views import Index, CantidadEdo, GraficasPorEstadoView, GetTagsCommon, RecursoFilterView
from ObservatorioTTApp import views
from ObservatorioTTApp.router import router

urlpatterns = [
    path('', Index.as_view(),name="AnaliticaIndex"),
    path('data/edos', CantidadEdo,name="Cantidad"),
    path('data/tags', GetTagsCommon,name="tagsStadist"),
    path('reportes/edo', GraficasPorEstadoView.as_view(),name="GEstado"),
    path('reportes/nac', RecursoFilterView.as_view(),name="GNacional")


]
