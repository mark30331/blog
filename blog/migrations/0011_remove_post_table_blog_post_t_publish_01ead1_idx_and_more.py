# Generated by Django 5.0.4 on 2024-06-14 19:59

import taggit.managers
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_post_table_blog_post_t_publish_bd5c03_idx_and_more'),
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='post_table',
            name='blog_post_t_publish_01ead1_idx',
        ),
        migrations.AddField(
            model_name='post_table',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddIndex(
            model_name='post_table',
            index=models.Index(fields=['-publish'], name='blog_post_t_publish_bd5c03_idx'),
        ),
    ]
