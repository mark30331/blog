# Generated by Django 5.0.4 on 2024-04-17 20:13

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_post_posts_table'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts_table',
            options={'ordering': ['-publish']},
        ),
        migrations.AddField(
            model_name='posts_table',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='posts_table',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='posts_table',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='posts_table',
            name='status',
            field=models.CharField(choices=[('DF', 'Draft'), ('PB', 'Published')], default='DF', max_length=2),
        ),
        migrations.AddField(
            model_name='posts_table',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddIndex(
            model_name='posts_table',
            index=models.Index(fields=['-publish'], name='blog_posts__publish_861810_idx'),
        ),
    ]
