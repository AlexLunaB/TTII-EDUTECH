# Generated by Django 3.1.3 on 2021-01-06 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0011_auto_20210105_0613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recurso',
            name='categoria',
        ),
        migrations.AlterField(
            model_name='recursosarchivo',
            name='recurso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recurso_img', to='recursos.recurso'),
        ),
        migrations.AlterField(
            model_name='recursosarchivo',
            name='tipo',
            field=models.CharField(choices=[('IMG', 'IMG'), ('VID', 'VID')], default='IMG', max_length=3),
        ),
    ]