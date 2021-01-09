from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

# Declarando Preferencias
from taggit.managers import TaggableManager

from ObservatorioTTApp.models import MexicoState, MexicoMunicipio


PERMISO_USUARIO = (
  ("AD", "Administrador"),
  ("GE", "General"),
  ("IN", "Investigador"),
)


class Usuario(AbstractUser):
  permiso = models.CharField(max_length=20, choices=PERMISO_USUARIO, default='GE')

  def __str__(self):
    return self.username


class Profile(models.Model):
  usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE,
                                 primary_key=True,
                                 )

  estado= models.ForeignKey(MexicoState, on_delete=models.CASCADE,null=True)
  semblanza= models.CharField(max_length=1000,null=True)
  municipio = models.ForeignKey(MexicoMunicipio, on_delete=models.CASCADE,null=True)
  telefono=  models.CharField(max_length=12,null=True)
  foto= models.ImageField(upload_to="Perfil_Fotos",null=True)
  intereses = TaggableManager(through="recursos.TaggedWhatever", )



