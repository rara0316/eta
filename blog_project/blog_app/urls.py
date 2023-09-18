from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import image_upload, CreateOrUpdatePostView


app_name = 'blog_app'
urlpatterns = [
    path('',views.post_list, name='post_list'),
    path('post_list/<str:topic>/', views.post_list, name='post_list_by_topic'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('edit_post/<int:post_id>/',CreateOrUpdatePostView.as_view(), name='edit_post'),

    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # write part
    path('write/',CreateOrUpdatePostView.as_view(), name='create_or_update_post'),
    path('image-upload/', image_upload, name='image_upload'),   


]