from django.contrib import admin
from .models import Recurso

# Register your models here.

class RecursoAdmin(admin.ModelAdmin):
    readonly_fields = ('fechaCreacion', 'fechaModificacion')

admin.site.register(Recurso, RecursoAdmin)