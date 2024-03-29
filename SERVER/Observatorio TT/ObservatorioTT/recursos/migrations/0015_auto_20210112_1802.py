# Generated by Django 3.1.5 on 2021-01-12 18:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recursos', '0014_recurso_html'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recursosarchivo',
            name='tipo',
            field=models.CharField(choices=[('IMG', 'IMG'), ('VID', 'VID')], default='IMG', max_length=3),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=1000)),
                ('recurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recursos.recurso')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
