from django.db import models

# Create your models here.
class blog_project_account(models.Model):
    account = models.CharField(max_length=100)