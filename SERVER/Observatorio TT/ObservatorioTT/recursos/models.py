from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
from taggit.managers import TaggableManager
from taggit.models import GenericTaggedItemBase, TagBase

from ObservatorioTTApp.models import MexicoMunicipio,MexicoState
from usuarios.models import Usuario
import numpy as np

class Categoria(models.Model):
  descripcion= models.CharField(max_length=100)
  def __str__(self):
    return self.descripcion



class MyCustomTag(TagBase):
    # ... fields here

    class Meta:
      verbose_name = ("Tag")
      verbose_name_plural = ("Tags")

    # ... methods (if any) here


class TaggedWhatever(GenericTaggedItemBase):
  # TaggedWhatever can also extend TaggedItemBase or a combination of
  # both TaggedItemBase and GenericTaggedItemBase. GenericTaggedItemBase
  # allows using the same tag for different kinds of objects, in this
  # example Food and Drink.

  # Here is where you provide your custom Tag class.
  tag = models.ForeignKey(
    MyCustomTag,
    on_delete=models.CASCADE,
    related_name="%(app_label)s_%(class)s_items",
  )


class Recurso(models.Model):
    nombreRecurso = models.CharField(max_length = 50)

    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estado= models.ForeignKey(MexicoState, on_delete=models.CASCADE)
    municipio= models.ForeignKey(MexicoMunicipio, on_delete=models.CASCADE)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaModificacion = models.DateTimeField(auto_now=True)
    descripcion = models.CharField(max_length = 250)
    tags = TaggableManager(through=TaggedWhatever)


    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'recurso'
        verbose_name_plural = 'recursos'

    def __str__(self):
        return self.nombreRecurso

    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.rating_set.all())
        return np.mean(all_ratings)


class RecursosArchivo(models.Model):
  IMG= "IMG"
  VID= "VID"
  Options={
    (IMG,IMG),
    (VID,VID)
  }
  archivo= models.FileField(upload_to="Archivos")
  tipo= models.CharField(choices=Options,default=IMG,max_length=3)
  recurso= models.ForeignKey(Recurso, on_delete=models.CASCADE ,related_name='recurso_img')



class Rating(models.Model):
  RATING_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
  )
  user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
  user_name = models.CharField(max_length=100,null=True)
  comment = models.CharField(max_length=200,null=True)
  pub_date = models.DateTimeField('date published', auto_now_add=True,null=True)
  recurso = models.ForeignKey(Recurso, on_delete=models.CASCADE)
  rating = models.IntegerField(default=1, choices=RATING_CHOICES)

class Cluster(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(Usuario)

    def get_members(self):
      return "\n".join([u.username for u in self.users.all()])
