from django.shortcuts import render
from .forms import BlogPostForm
from django.views import View
from django.core.files.storage import default_storage
from django.conf import settings
from django.http import JsonResponse

# Create your views here.
# Create your views here.
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