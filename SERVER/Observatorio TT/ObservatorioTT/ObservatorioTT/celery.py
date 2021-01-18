from __future__ import absolute_import, unicode_literals
import os

# Establecer las opciones de django para la aplicación de celery.
from celery.app import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ObservatorioTT.settings')

# Crear la aplicación de Celery
app = Celery('ObservatorioTT')

# Especificamos que las variables de configuración de Celery se encuentran
# en el fichero `settings.py` de Django.
# El parámetro namespace es para decir que las variables de configuración de
# Celery en el fichero settings empiezan por el prefijo *CELERY_*
app.config_from_object('django.conf:settings')
# Este método auto-registra las tareas para el broker.
# Busca tareas dentro de todos los archivos `tasks.py` que haya en las apps
# y las envía a Redis automáticamente.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS) #Nota 5

app.conf.update(BROKER_URL='redis://127.0.0.1:6379')

CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
