from django.contrib import admin
from .models import Recurso, Categoria, Rating, RecursosArchivo

# Register your models here.





admin.site.register(Recurso)
admin.site.register(RecursosArchivo)
admin.site.register(Rating)
admin.site.register(Categoria)
