from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import image_upload


app_name = 'blog_app'
urlpatterns = [
    path('',views.post_list, name='post_list'),
    path('post_list/<str:topic>/', views.post_list, name='post_list_by_topic'),

    path('post/<int:post_id>/', views.post_detail, name='post_detail'),

    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # write part
    path('write/', views.write),
    path('image-upload/', image_upload.as_view(), name='image-upload'),

]