from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import image_upload


app_name = 'blog_app'
urlpatterns = [
    path('',views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # write part
    path('write/', views.write),
    path('image-upload/', image_upload.as_view(), name='image-upload'),

    path('post_list/', views.post_list, name='post_list'),
]