from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import image_upload, CreateOrUpdatePostView


app_name = 'blog_app'
urlpatterns = [
    path('',views.post_list, name='post_list'),
    path('post_list/<str:topic>/', views.post_list, name='post_list_by_topic'),

    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # write part
    path('image-upload/', image_upload.as_view(), name='image_upload'),

    path('write/',CreateOrUpdatePostView.as_view(), name='create_or_update_post'),
]