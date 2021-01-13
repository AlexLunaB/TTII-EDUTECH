from django.db import models

# Create your models here.
from taggit.managers import TaggableManager

from recursos.models import TaggedWhatever
from usuarios.models import Usuario


class ForoDiscusion(models.Model):
    temaDiscusion = models.CharField(max_length = 500)
    descripcion = models.CharField(max_length = 250)
    Imagen= models.ImageField(upload_to="Blog")
    html= models.TextField()
    administrador = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = TaggableManager(through=TaggedWhatever)


    class Meta:
        verbose_name = 'foroDiscusion'
        verbose_name_plural = 'forosDiscusion'

    def __str__(self):
        return self.temaDiscusion



class ComentarioBlog(models.Model):
  fecha= models.DateTimeField(auto_now_add=True,null=True)
  comentario = models.CharField(max_length=1000)
  recurso = models.ForeignKey(ForoDiscusion, on_delete=models.CASCADE)
  usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
