from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from rest_framework import generics
from .serializers import BlogPostSerializer
from django.conf import settings
from django.views import View

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

class CreateOrUpdatePostView(View):
    template_name = 'blog_app/write.html'
    
def get(self, request, post_id =None):
    post = get_object_or_404(BlogPost, id=post_id) if post_id else None
    form = BlogPostForm(instance=post)
    context = {'form': form, 'post':post, 'edit_mode':post_id is not Null, 'MEDIA_URL':settings.MEDIA_URL}
    return render(request, self.template_name, context)

def post(self, request, post_id=None):
    post = get_object_or_404(BlogPost,id=post_id) if post_id else None
    form = BlogPostForm(instance=post)
    
    if form.is_valid():
        post = form.save(commit=False)
        
        if 'delete-button' in request.POST:
            post.delete()
            return redirect('blog_app:post_list')
        post.category = '전체' if not form.cleaned_data.get('topic') else form.cleaned_data.get('topic')
        post.publish = 'N' if 'temp-save-button' in request.POST else 'Y'
        post.author_id = request.user.username
        post.save()
        return redirect('blog_app:post_detail', post_id=post.id)
        
    context = {'form': form, 'post':post, 'edit_mode':post_id is not Null, 'MEDIA_URL':settings.MEDIA_URL}
    return render(request, self.template_name, context)
            