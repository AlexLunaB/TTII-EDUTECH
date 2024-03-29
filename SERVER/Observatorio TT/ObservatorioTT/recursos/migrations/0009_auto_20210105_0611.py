# Generated by Django 3.1.3 on 2021-01-05 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('recursos', '0008_auto_20210105_0606'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyCustomTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.RemoveField(
            model_name='recurso',
            name='tags',
        ),
        migrations.AlterField(
            model_name='recursosarchivo',
            name='tipo',
            field=models.CharField(choices=[('VID', 'VID'), ('IMG', 'IMG')], default='IMG', max_length=3),
        ),
        migrations.CreateModel(
            name='TaggedWhatever',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='object ID')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recursos_taggedwhatever_tagged_items', to='contenttypes.contenttype', verbose_name='content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recursos_taggedwhatever_items', to='recursos.mycustomtag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
