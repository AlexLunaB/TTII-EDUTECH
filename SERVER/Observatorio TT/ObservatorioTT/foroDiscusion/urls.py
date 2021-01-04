from django.conf import settings
from django.urls import path, include
from django.views import static

from foroDiscusion.router import router

urlpatterns = [
    path('api/', include(router.urls),name="Observatorio_api")
]
