from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    topic = models.CharField(max_length=255, default='전체')
    publish = models.CharField(max_length=1, default='Y')
    views = models.IntegerField(default=0)
    author_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # '..' 문자열이 포함된 content 필드를 변경
        self.content = self.content.replace('"..', '"')
        super().save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    author = models.CharField(max_length=255, default="User")  # 기본값을 "User"로 설정
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

class ImageId(models.Model):
    
    image = models.ImageField(upload_to = "images/", null=True, blank=True)

class TitleImageId(models.Model):
    pass

    
