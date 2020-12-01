# Generated by Django 3.1.3 on 2020-11-16 07:03

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreRecurso', models.CharField(max_length=50)),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('fechaModificacion', models.DateTimeField(auto_now=True)),
                ('descripcion', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'recurso',
                'verbose_name_plural': 'recursos',
            },
        ),
        migrations.CreateModel(
            name='RecursosArchivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo', models.FileField(upload_to='Archivos')),
                ('tipo', models.CharField(choices=[('IMG', 'IMG'), ('VID', 'VID')], default='IMG', max_length=3)),
                ('recurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recursos.recurso')),
            ],
        ),
    ]
