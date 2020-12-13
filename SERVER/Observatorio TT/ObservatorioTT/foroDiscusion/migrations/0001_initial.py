# Generated by Django 3.1.3 on 2020-11-16 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ForoDiscusion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temaDiscusion', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=250)),
                ('administrador', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'foroDiscusion',
                'verbose_name_plural': 'forosDiscusion',
            },
        ),
    ]