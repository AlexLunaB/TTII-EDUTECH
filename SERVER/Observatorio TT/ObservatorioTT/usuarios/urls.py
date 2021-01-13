from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from usuarios.router import router
from usuarios.views import ProfileUsers, MyTokenObtainPairView

urlpatterns = [
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/Profile/', ProfileUsers.as_view(), name='Profile'),
    path('', include(router.urls),name="usuario_api"),


]
