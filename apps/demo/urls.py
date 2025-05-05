# apps/demo/urls.py

from django.urls import path
from apps.demo.views import demo_view

urlpatterns = [
    path('', demo_view, name='demo'),
]
