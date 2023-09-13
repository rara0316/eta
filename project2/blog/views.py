from django.shortcuts import render, redirect, authenticate
from .serializers import BlogPostSerializer
from .forms import CustomLoginForm, BlogPostForm

# Create your views here.
def index(request):
    return render(request, 'board-client.html')

def write(request):
    return render(request, 'write.html')

# 로그인
def custom_login(request):
    if request.user.is_authenticated:
        return redirect('blog_app:post_list')
    else:
        form = CustomLoginForm(data=request.POST or None)  # 커스텀 로그인 폼 사용
        if request.method == "POST":
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('blog_app:post_list')  # 슈퍼유저와 일반 사용자 모두 동일한 페이지로 리다이렉션
        return render(request, 'registration/login.html', {'form': form})