# Generated by Django 4.2.4 on 2023-09-19 14:49

from django.db import migrations, models
import django_ckeditor_5.fields


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
                ('content', django_ckeditor_5.fields.CKEditor5Field(verbose_name='text')),
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
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='TitleImageId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
