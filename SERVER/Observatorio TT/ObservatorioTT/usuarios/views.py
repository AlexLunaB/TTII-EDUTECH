from django.shortcuts import render

# Create your views here.
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

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

#Obtiene el token con el que se trabajará
class TokenGetWithUserSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        # Add extra responses here
        data['user'] = UserModelSerializer(self.user).data,
        data['groups'] = self.user.groups.values_list('name', flat=True)
        return data

class MyTokenObtainPairView(TokenObtainPairView):
      serializer_class = TokenGetWithUserSerializer

class UserViewSet(
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet,

                  ):
    """User view set.
    Handle sign up, login and account verification.
    """

    queryset = Usuario.objects.filter(is_active=True)
    serializer_class = UserModelSerializer
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


    @action(detail=False, methods=['put', 'patch','get'])
    def profile(self, request, *args, **kwargs):
        """Update profile data."""
        user = request.user
        profile = user.profile

        if request.method=="PATCH" or  request.method=="PUT":

          #actualizaFoto
          print(request.data)
          partial = request.method == 'PATCH'

          serializer = ProfileModelSerializer(
            profile,
            data=request.data["usuario"]["profile"],
            partial=partial
          )

          userserializer= UserModelSerializer(
            user,
            data=request.data["usuario"],
            partial=partial
          )
          userserializer.is_valid()
          userserializer.save()
          serializer.is_valid()
          serializer.save()
          data = UserModelSerializer(user, context={"request": request}).data
          return Response(data)

        else:
          data = UserModelSerializer(user, context={"request":request}).data
          return Response(data)
    @action(detail=False, methods=['put', 'patch','get'])
    def foto(self, request, *args, **kwargs):
        """Update profile data."""
        user = request.user
        profile = user.profile
        if request.method=="PATCH" or  request.method=="PUT":
          print(request.data)
          imagen=self.request.data["foto"]

          if imagen:
            print(imagen)
            profile.foto=imagen
            profile.save()

            data = UserModelSerializer(user, context={"request": request}).data
            return Response(data)
          else:
            return Response(status=400,data={"msj":"No se adjunto una imagen"})



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
