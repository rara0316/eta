from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomLoginForm
from .models import BlogPost
from django.core.files.storage import default_storage
from django.conf import settings
from django.http import JsonResponse
from .forms import BlogPostForm
from django.views import View

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

def write(request):
    form = BlogPostForm()
    return render(request, 'write.html', {'form': form})

#이미지 업로드
class image_upload(View):
    # 이미지 업로드 버튼 눌렀을 떄
    def post(self, request):
        file = request.FILES['file']
        # 파일경로설정
        filepath = 'uploads/' + file.name
        print(filepath)
        # 파일이름설정
        filename = default_storage.save(filepath, file)
        # 파일URL 만들기
        file_url = settings.MEDIA_URL + filename
        # 이미지 업로드가 끝나면 JSON으로 이미지 파일 url 변환
        return JsonResponse({'location': file_url})
