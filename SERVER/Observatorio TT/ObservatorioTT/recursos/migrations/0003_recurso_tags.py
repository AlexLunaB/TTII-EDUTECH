# Generated by Django 3.1.3 on 2020-11-25 18:33

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('recursos', '0002_auto_20201116_0703'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurso',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
