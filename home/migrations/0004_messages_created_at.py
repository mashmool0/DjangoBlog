# Generated by Django 5.0.4 on 2024-05-07 14:55

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_messages_alter_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
