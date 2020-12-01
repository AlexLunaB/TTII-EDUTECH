from django.db import models

# Create your models here.



class MexicoState(models.Model):

  id= models.CharField( max_length=3,primary_key=True)
  nombre= models.CharField(max_length=50)

class MexicoMunicipio(models.Model):
  estado= models.ForeignKey(MexicoState, on_delete=models.CASCADE)
  nombre= models.CharField(max_length=60)
  def __str__(self):
    return self.nombre
