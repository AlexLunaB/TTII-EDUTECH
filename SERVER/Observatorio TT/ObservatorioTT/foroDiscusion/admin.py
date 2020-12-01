from django.contrib import admin
from .models import ForoDiscusion

# Register your models here.

class ForoDiscusionAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(ForoDiscusion, ForoDiscusionAdmin)
