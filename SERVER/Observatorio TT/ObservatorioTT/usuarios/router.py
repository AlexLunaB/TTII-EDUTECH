from rest_framework import routers

from usuarios.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'View', UserViewSet)
