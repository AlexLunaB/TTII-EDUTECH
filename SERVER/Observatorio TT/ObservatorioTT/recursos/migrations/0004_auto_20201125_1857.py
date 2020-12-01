# Generated by Django 3.1.3 on 2020-11-25 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0003_recurso_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='comment',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='rating',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='date published'),
        ),
        migrations.AddField(
            model_name='rating',
            name='user_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1),
        ),
        migrations.AlterField(
            model_name='recursosarchivo',
            name='tipo',
            field=models.CharField(choices=[('VID', 'VID'), ('IMG', 'IMG')], default='IMG', max_length=3),
        ),
    ]
