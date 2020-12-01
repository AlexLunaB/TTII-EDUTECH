from django.urls import path, include

from ObservatorioTTApp import views
from ObservatorioTTApp.router import router

urlpatterns = [
    path('api/', include(router.urls),name="Observatorio_api")
]
