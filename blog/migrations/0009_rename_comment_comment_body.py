# Generated by Django 4.2.9 on 2024-02-08 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_featured_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='body',
        ),
    ]
