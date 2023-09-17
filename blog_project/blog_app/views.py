from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomLoginForm
from .models import BlogPost

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect('blog_app:login')
    
    else :
        form = CustomLoginForm(data=request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None and user.is_superuser:  # 슈퍼유저 계정 확인
                    login(request, user)
                    return redirect('blog_app:login')  # 로그인 후 이동할 페이지 이름
                else:
                    # 슈퍼유저 계정이 아닌 경우 에러 메시지 처리
                    form.add_error(None, "다시 입력해주세요.")

    return render(request, 'login.html', {'form': form})





