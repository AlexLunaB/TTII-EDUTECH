from django.urls import path, include

from recursos.router import router

urlpatterns = [    path('api/', include(router.urls),name="recursos_api"),
]



