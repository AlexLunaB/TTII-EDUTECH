from django.db import models

# Create your models here.



class MexicoState(models.Model):

  id= models.CharField( max_length=3,primary_key=True)
  nombre= models.CharField(max_length=50)


  def __str__(self):
    return self.nombre

class MexicoMunicipio(models.Model):
  estado= models.ForeignKey(MexicoState, on_delete=models.CASCADE)
  nombre= models.CharField(max_length=200)
  def __str__(self):
    return self.nombre

class IntitucionEmpresa(models.Model):
  NombreInstitucion= models.CharField(max_length=100)
  Imagen= models.ImageField(upload_to="LogosInstitutos")
