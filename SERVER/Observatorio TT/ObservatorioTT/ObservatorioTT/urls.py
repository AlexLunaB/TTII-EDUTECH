"""ObservatorioTT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconfusuar
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# from ObservatorioTTApp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Copiar path tantas aplicaciones como se tengan
    path('', include('ObservatorioTTApp.urls')),

    path('Recursos/', include(('recursos.urls', 'recursos'), namespace='recursos')),
<<<<<<< HEAD
    path('Usuarios/', include(('usuarios.urls', 'usuarios'), namespace='usuarios')),
]
=======
    path('Usuarios/', include(('usuarios.urls', 'usuarios'), namespace='recursos')),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
>>>>>>> 7b319c808a79d7b0f0b037a9f7e648fb226aba9f
