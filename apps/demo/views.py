# apps/demo/views.py

from django.shortcuts import render

def demo_view(request):
    return render(request, 'demo/home.html')


# apps/demo/views.py

from django.shortcuts import render

def demo_view(request):
    return render(request, 'demo/home.html')  # Головна сторінка для демонстрації
