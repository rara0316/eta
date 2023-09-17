# Generated by Django 4.2.5 on 2023-09-17 13:09

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('topic', models.CharField(default='전체', max_length=255)),
                ('publish', models.CharField(default='Y', max_length=1)),
                ('views', models.IntegerField(default=0)),
                ('author_id', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImageId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TitleImageId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]