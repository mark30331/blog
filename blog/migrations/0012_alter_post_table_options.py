# Generated by Django 5.0.4 on 2024-08-09 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_remove_post_table_blog_post_t_publish_01ead1_idx_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post_table',
            options={'ordering': ['publish'], 'verbose_name': 'post'},
        ),
    ]
