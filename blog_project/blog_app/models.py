from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, default='전체')
    temporary = models.CharField(max_length=1, default='Y') # 임시저장
    views = models.PositiveIntegerField(default=0)
    author_id = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
    