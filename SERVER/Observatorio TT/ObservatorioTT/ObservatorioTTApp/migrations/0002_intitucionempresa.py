# Generated by Django 3.1.5 on 2021-01-10 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ObservatorioTTApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntitucionEmpresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreInstitucion', models.CharField(max_length=100)),
                ('Imagen', models.ImageField(upload_to='LogosInstitutos')),
            ],
        ),
    ]
