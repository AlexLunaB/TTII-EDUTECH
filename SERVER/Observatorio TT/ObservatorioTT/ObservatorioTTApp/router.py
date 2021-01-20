from rest_framework import routers

from ObservatorioTTApp.views import EstadosMexicoViewSet, InstitucionesViewSet
from recursos.views import RecursoViewSet, CategoriaViewSet

router = routers.DefaultRouter()

router.register(r'Estados', EstadosMexicoViewSet)
router.register(r'Instituciones', InstitucionesViewSet)

