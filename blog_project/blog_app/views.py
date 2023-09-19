from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomLoginForm, CommentForm
from .models import BlogPost, Comment
from django.core.files.storage import default_storage
from django.conf import settings
from django.http import JsonResponse
from .forms import BlogPostForm
from django.views import View
from rest_framework import generics
from .serializers import BlogPostSerializer
from bs4 import BeautifulSoup
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.files.storage import FileSystemStorage  
import openai  # GPT-3 라이브러리

# Create your views here.

# 첫화면으로 보여줄 화면입니다. post_list를 대신해 임시로 넣었습니다.
# post_list.html링크를 수정할 필요가 있습니다.
# def index(request):
#     # 게시글 오브젝트
#     BlogPosts = BlogPost.objects.all() 
#     posts = {'posts':BlogPosts}
#     return render(request,'index.html', posts)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('blog_app:post_list')
    
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

def post_list(request,topic=None):
    if topic:
        posts = BlogPost.objects.filter(topic=topic, publish='Y').order_by('-views')
    else:
        posts = BlogPost.objects.filter(publish='Y').order_by('-views')
    # dict형식을 잘못 작성하고 있었습니다.
    posts = {
        'posts': posts,
    }
    return render(request, 'post_list.html', posts)





# 포스트 restful api 뷰 생성
class BlogPostList(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class CreateOrUpdatePostView(View):
    template_name = 'write.html'
    
    def get(self, request, post_id =None):
        post = get_object_or_404(BlogPost, id=post_id) if post_id else None
        form = BlogPostForm(instance=post)
        context = {'form': form, 'post':post, 'edit_mode':post_id is not None, 'MEDIA_URL':settings.MEDIA_URL}
        print("getgetgetegetegetetegegegegegegegege")
        return render(request, self.template_name, context)

    def post(self, request, post_id=None):
        post = get_object_or_404(BlogPost,id=post_id) if post_id else None
        form = BlogPostForm(request.POST, instance=post)
        print("postpostpsotpsotpsotpsotpsotpsotpsotpsotpsotsp")

        if form.is_valid():
            post = form.save(commit=False)
                    
            if 'delete-button' in request.POST:
                            post.delete()
                            return redirect('blog_app:post_list')
            post.topic = request.POST['topic'] 
            post.publish = 'N' if 'temp-save-button' in request.POST else 'Y'
            post.author_id = request.user.username
            post.save()
            return redirect('blog_app:post_detail', post_id=post.id)

        context = {'form': form, 'post':post, 'edit_mode':post_id is not None, 'MEDIA_URL':settings.MEDIA_URL}
        return render(request, self.template_name, context)
    

# def edit(request,  post_id =None):
#         # 객체 가져오기
#         post = get_object_or_404(BlogPost, pk=post_id)
 
#         # 유저 다르면 돌려보내기
#         # if blog.username != request.user.username:
#         #       return redirect('home')
 
#         # 입력된 내용 처리 -> POST
#         if request.method == 'POST':
#                 form = BlogPost(request.POST or None, instance=blog)
#                 if form.is_valid(): # 잘입력된지 체크
#                         post = form.save(commit=False)
#                         post.save() # 저장하기
#                         return redirect('/blog/'+str(blog.id))
 
#         # 빈 페이지 띄워주는 기능 -> GET
#         else :
#                 form = BlogPost(instance=blog)
#                 return render(request, 'edit.html', {'blog':blog,'form':form})

#댓글 추가
def add_comment(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()

            # 댓글을 저장한 후 해당 게시물 상세 페이지로 리디렉션
            return redirect(reverse('blog_app:post_detail', args=[post_id]))
    else:
        form = CommentForm()

    # 댓글 작성에 실패하면 여기로 돌아갈 수 있도록 설정할 수 있습니다.
    return redirect(reverse('blog_app:post_detail', args=[post_id]))

#이미지 업로드

def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    if request.method == 'POST': 

        # 요청에 삭제가 포함된경우
        if 'delete-button' in request.POST:
            post.delete()
            return redirect('blog_app:post_list')

    # 조회수 증가 및 db에 저장
    post.views += 1 
    post.save() 

    # 이전/다음 게시물 가져옴
    previous_post = BlogPost.objects.filter(id__lt=post.id, publish='Y').order_by('-id').first()
    next_post = BlogPost.objects.filter(id__gt=post.id, publish='Y').order_by('id').first()

    # 같은 주제인 게시물들 중 최신 글 가져옴
    recommended_posts = BlogPost.objects.filter(topic=post.topic, publish='Y').exclude(id=post.id).order_by('-created_at')[:2]
    # 게시물 내용에서 첫번째 이미지(썸네일) 태그 추출
    for recommended_post in recommended_posts:
        soup = BeautifulSoup(recommended_post.content, 'html.parser')
        image_tag = soup.find('img')
        recommended_post.image_tag = str(image_tag) if image_tag else ''
    
    comments = Comment.objects.filter(post=post).order_by('-created_date')
    
    context = {
        'post': post,
        'previous_post': previous_post,
        'next_post': next_post,
        'recommended_posts': recommended_posts,
        'MEDIA_URL': settings.MEDIA_URL,
        'comments': comments,
        'form': CommentForm(),
    }

    return render(request, 'post.html', context)


def image_upload(request):
    file = request.FILES['file']
    # 파일경로설정
    filepath = 'uploads/' + file.name
    # 파일이름설정
    filename = default_storage.save(filepath, file)
    # 파일URL 만들기
    file_url = settings.MEDIA_URL + filename
    # 이미지 업로드가 끝나면 JSON으로 이미지 파일 url 변환
    return JsonResponse({'location': file_url})


# Chat gpt API 사용
openai.api_key = ''

# 글 자동완성 기능
def autocomplete(request):
    if request.method == "POST":

        #제목 필드값 가져옴
        prompt = request.POST.get('title')
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt},
                ],
            )
            # 반환된 응답에서 텍스트 추출해 변수에 저장
            message = response['choices'][0]['message']['content']
        except Exception as e:
            message = str(e)
        return JsonResponse({"message": message})
    return render(request, 'autocomplete.html')