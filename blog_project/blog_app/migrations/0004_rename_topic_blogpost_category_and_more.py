# Generated by Django 4.2.5 on 2023-09-15 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_remove_blogpost_category_remove_blogpost_temporary_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='topic',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='publish',
            new_name='temporary',
        ),
    ]