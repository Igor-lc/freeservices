from django.urls import path
from . import views

urlpatterns = [
    path('', views.map_view, name='gps_map'),
    path('api/track/', views.track_api, name='track_api'),
]
