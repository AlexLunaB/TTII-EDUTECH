from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from usuarios.models import Usuario
from usuarios.serializers import UserSerializer, ProfileSerializer

"""Users views."""

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)




class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet,
                  mixins.ListModelMixin):
    """User view set.
    Handle sign up, login and account verification.
    """

    queryset = Usuario.objects.filter(is_active=True)
    serializer_class = UserSerializer
    lookup_field = 'username'
    def list(self, request, *args, **kwargs):
      pass

class ProfileUsers(APIView):
      """
      View to list all users in the system.

      * Requires token authentication.
      * Only admin users are able to access this view.
      """

      def get(self, request, format=None):

        usuario=self.request.user
        perfil= usuario.profile
        d=ProfileSerializer(perfil, context={"request":request})
        return Response(data=d.data)
