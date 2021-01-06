from django.shortcuts import render

# Create your views here.
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView

from recursos.Serializers.RecursoSerializer import TagSerializer
from usuarios.models import Usuario, Profile
from usuarios.serializers import UserSerializer, ProfileSerializer, ProfileModelSerializer, UserModelSerializer, \
  UserSignUpSerializer

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
                  ):
    """User view set.
    Handle sign up, login and account verification.
    """

    queryset = Usuario.objects.filter(is_active=True)
    serializer_class = UserSerializer
    lookup_field = 'username'



    @action(detail=False, methods=['get'])
    def Tags(self, request):
      tags = Profile.intereses.all()
      print(tags)
      ts = TagSerializer(data=tags, many=True)
      print(ts.is_valid())
      print(ts.errors)
      return Response(ts.data)

    @action(detail=False, methods=['post'])
    def signup(self, request):
      """User sign up."""
      serializer = UserSignUpSerializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      user = serializer.save()
      data = UserModelSerializer(user).data
      return Response(data, status=status.HTTP_201_CREATED)


    @action(detail=False, methods=['put', 'patch'])
    def profile(self, request, *args, **kwargs):
        """Update profile data."""
        user = request.user
        profile = user.profile
        partial = request.method == 'PATCH'
        serializer = ProfileModelSerializer(
            profile,
            data=request.data,
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = UserModelSerializer(user).data
        return Response(data)

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
