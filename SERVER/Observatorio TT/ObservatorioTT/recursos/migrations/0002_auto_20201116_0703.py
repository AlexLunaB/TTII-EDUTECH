# Generated by Django 3.1.3 on 2020-11-16 07:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ObservatorioTTApp', '0001_initial'),
        ('recursos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurso',
            name='Usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='recurso',
            name='categoria',
            field=models.ManyToManyField(to='recursos.Categoria'),
        ),
        migrations.AddField(
            model_name='recurso',
            name='origen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ObservatorioTTApp.mexicomunicipio'),
        ),
        migrations.AddField(
            model_name='rating',
            name='recurso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recursos.recurso'),
        ),
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]