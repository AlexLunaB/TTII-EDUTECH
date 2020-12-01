from rest_framework import routers

from ObservatorioTTApp.views import EstadosMexicoViewSet
from recursos.views import RecursoViewSet, CategoriaViewSet

router = routers.DefaultRouter()

router.register(r'Estados', EstadosMexicoViewSet)

