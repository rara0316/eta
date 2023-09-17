from django.urls import path
from . import views
from .views import image_upload


urlpatterns = [
    # write part
    path('write/', views.write),
    path('image-upload/', image_upload.as_view(), name='image-upload')
]