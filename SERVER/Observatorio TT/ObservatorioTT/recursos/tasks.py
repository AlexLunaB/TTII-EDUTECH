# Create your tasks here
from __future__ import absolute_import, unicode_literals

import string
from datetime import timedelta
import random

import jwt
import redis
import six
from asgiref.sync import async_to_sync
from celery import shared_task, app
from celery.task import periodic_task, task
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template import loader, Context
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.encoding import force_bytes
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode
from jwt import PyJWT
from numpy import savetxt, save

from ObservatorioTT import settings

from time import sleep

from ObservatorioTTApp.recomendador import Myrecommend
from usuarios.models import Usuario


@shared_task
def mul(x, y):
    sleep(10)
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@task(bind=True)
def test():
    print("holaa")




def mandacorreo(user, servicio):
    account_activation_token = PasswordResetTokenGenerator()
    current_site = "127.0.0.1"
    t = loader.get_template('email/template.html')
    subject = 'Tienes una tarea pendiente'
    html_message = t.render({'servicio': servicio,
                             'user': user,
                             'domain': current_site,
                             'uid': servicio.pk,
                             'token': account_activation_token.make_token(servicio),
                             })
    plaintxt = strip_tags(html_message)
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, plaintxt, email_from, ["alexlb642@gmail.com", ], html_message=html_message)


def GeneraMatrizPrediccion():
  ma, mb = Myrecommend()

  print(ma)

  savetxt(settings.MEDIA_ROOT + '/data1.csv', ma, delimiter=',')


import datetime

@shared_task
@periodic_task(run_every=timedelta(seconds=5))
def GeneraMatriz():
    ma,mb=Myrecommend()
    save(str(settings.BASE_DIR)+'/ma', ma)
    save(str(settings.BASE_DIR)+'/mb', mb)


def gen_verification_token(user):
  """Create JWT token that the user can use to verify its account."""
  exp_date = timezone.now() + timedelta(days=3)
  payload = {
    'user': user.username,
    'exp': int(exp_date.timestamp()),
    'type': 'email_confirmation'
  }

  token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
  return token.decode()


@task(name='send_confirmation_email', max_retries=3)
def send_confirmation_email(user_pk):
    """Send account verification link to given user."""
    user = Usuario.objects.get(pk=user_pk)
    verification_token = gen_verification_token(user)
    subject = 'Bienvenido @{}! Verifica tu cuenta para empezar a utilizar tu cuenta en el Observatorio'.format(user.username)
    from_email = 'alexlb642@gmail.com'
    content = render_to_string(
        'emails/users/account_verification.html',
        {'token': verification_token, 'user': user}
    )
    msg = EmailMultiAlternatives(subject, content, settings.EMAIL_HOST_USER, [user.email])
    msg.attach_alternative(content, "text/html")
    msg.send()

