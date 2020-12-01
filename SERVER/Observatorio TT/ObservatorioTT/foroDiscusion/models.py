from django.db import models

# Create your models here.

class ForoDiscusion(models.Model):
    temaDiscusion = models.CharField(max_length = 50)
    descripcion = models.CharField(max_length = 250)
    administrador = models.CharField(max_length = 50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'foroDiscusion'
        verbose_name_plural = 'forosDiscusion'

    def __str__(self):
        return self.temaDiscusion
