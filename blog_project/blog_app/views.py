from django.shortcuts import render, redirect
from .models import BlogPost
from rest_framework import generics
from .serializers import BlogPostSerializer

# Create your views here.
def post_list(request):
    category = request.GET.get('category')
    if category:
        posts = BlogPost.objects.filter(category=category, publish='Y').order_by('-views')
    else:
        posts = BlogPost.objects.filter(publish='Y').order_by('-views')
    
    context = {
        'posts: posts',
    }
    return render(request, 'post_list.html', context)

# 포스트 restful api 뷰 생성
class BlogPostList(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer