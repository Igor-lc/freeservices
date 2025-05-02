from django.urls import path
from . import views
from .views import track_geojson_view

app_name = 'gps'

urlpatterns = [
    path('', views.map_view, name='gps_map'),
    # path('api/track/', views.track_api, name='track_api'),
    path("track/geojson/", track_geojson_view, name="track_geojson"),
]
