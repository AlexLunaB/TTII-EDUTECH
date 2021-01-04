# Generated by Django 3.1.3 on 2020-12-29 05:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('foroDiscusion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='forodiscusion',
            name='Imagen',
            field=models.ImageField(default=1, upload_to='Blog'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='forodiscusion',
            name='html',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='forodiscusion',
            name='administrador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='forodiscusion',
            name='temaDiscusion',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='forodiscusion',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
