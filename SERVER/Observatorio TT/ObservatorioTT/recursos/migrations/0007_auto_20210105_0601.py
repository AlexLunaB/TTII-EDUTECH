# Generated by Django 3.1.3 on 2021-01-05 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0006_auto_20210105_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recursosarchivo',
            name='tipo',
            field=models.CharField(choices=[('VID', 'VID'), ('IMG', 'IMG')], default='IMG', max_length=3),
        ),
    ]
