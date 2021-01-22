import jwt
from django.contrib.auth import password_validation
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from taggit_serializer.serializers import TagListSerializerField

from ObservatorioTT import settings
from usuarios.models import Usuario, Profile
from recursos.tasks import send_confirmation_email

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = Usuario
    fields = ("id","username")


class ProfileSerializer(serializers.ModelSerializer):
  usuario= UserSerializer
  class Meta:
    model = Profile
    fields = ("__all__")

class ProfileModelSerializer(serializers.ModelSerializer):
  intereses = TagListSerializerField()

  def create(self, validated_data):
    tags = validated_data.pop('intereses')
    if tags:
      tags = map(lambda x: x.capitalize(), tags)
    instance = super(ProfileModelSerializer, self).create(validated_data)
    instance.intereses.set(*tags)
    return instance
    """Profile model serializer."""
  def update(self, instance, validated_data):
    tags = validated_data.get('intereses')
    if tags:
      tags = validated_data.pop('intereses')
      tags = map(lambda x: x.capitalize(), tags)
    instance = super(ProfileModelSerializer, self).update(instance,validated_data)
    if tags:
      instance.intereses.set(*tags)
    return instance


  class Meta:
      """Meta class."""

      model = Profile
      fields = ('__all__')
      read_only_fields = (
        'foto',
      )




class UserModelSerializer(serializers.ModelSerializer):
  """User model serializer."""

  profile = ProfileModelSerializer(read_only=True)

  class Meta:
    """Meta class."""

    model = Usuario
    fields = (
      'username',
      'first_name',
      'last_name',
      'email',
      'profile'
      ,'permiso'
    )

class UserSignUpSerializer(serializers.Serializer):
    """User sign up serializer.

    Handle sign up data validation and user/profile creation.
    """

    email = serializers.EmailField(
      validators=[UniqueValidator(queryset=Usuario.objects.all())]
    )
    username = serializers.CharField(
      min_length=4,
      max_length=20,
      validators=[UniqueValidator(queryset=Usuario.objects.all())]
    )
    # Password
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)
    # Name
    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)

    def validate(self, data):
      """Verify passwords match."""
      passwd = data['password']
      passwd_conf = data['password_confirmation']
      if passwd != passwd_conf:
        raise serializers.ValidationError("Passwords don't match.")
      password_validation.validate_password(passwd)
      return data

    def create(self, data):
      """Handle user and profile creation."""
      data.pop('password_confirmation')
      user = Usuario.objects.create_user(**data)
      user.is_active=False
      user.save()
      Profile.objects.create(usuario=user)
      send_confirmation_email.delay(user_pk=user.pk)
      return user


class AccountVerificationSerializer(serializers.Serializer):
  """Account verification serializer."""

  token = serializers.CharField()

  def validate_token(self, data):
    """Verify token is valid."""
    try:
      payload = jwt.decode(data, settings.SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
      raise serializers.ValidationError('Verification link has expired.')
    except jwt.PyJWTError:
      raise serializers.ValidationError('Invalid token')
    if payload['type'] != 'email_confirmation':
      raise serializers.ValidationError('Invalid token')

    self.context['payload'] = payload
    return data

  def save(self):
    """Update user's verified status."""
    payload = self.context['payload']
    user = Usuario.objects.get(username=payload['user'])
    user.is_active = True
    user.save()
