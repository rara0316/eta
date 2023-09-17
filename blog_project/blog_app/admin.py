from django.contrib import admin

# Register your models here.
from .models import BlogPost

# 관리자 페이지에서 수정가능하도록
admin.site.register(BlogPost)