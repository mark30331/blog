# Generated by Django 5.0.4 on 2024-04-20 02:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_posts_table_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Posts_Table',
            new_name='Post_Table',
        ),
        migrations.RenameIndex(
            model_name='post_table',
            new_name='blog_post_t_publish_bd5c03_idx',
            old_name='blog_posts__publish_861810_idx',
        ),
    ]
