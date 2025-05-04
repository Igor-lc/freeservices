from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('download/', views.download_youtube_downloader, name='download_youtube_downloader'),
]
