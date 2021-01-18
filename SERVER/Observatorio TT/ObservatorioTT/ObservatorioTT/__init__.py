
# Esto sirve para que la aplicación de Celery se creé siempre
# que Django se inicie.
from .celery import app as celery_app

__all__ = ('celery_app',)
