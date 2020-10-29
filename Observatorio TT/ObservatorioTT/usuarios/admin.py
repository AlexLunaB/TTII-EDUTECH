from django.contrib import admin
from .models import Usuario

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Usuario, UsuarioAdmin)


