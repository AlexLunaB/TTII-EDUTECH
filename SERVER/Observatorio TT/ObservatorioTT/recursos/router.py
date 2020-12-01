from rest_framework import routers

from recursos.views import RecursoViewSet, CategoriaViewSet

router = routers.DefaultRouter()

router.register(r'Articulos', RecursoViewSet)
router.register(r'Categorias', CategoriaViewSet)

