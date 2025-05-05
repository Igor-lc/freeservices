# freeservices/freeservices/views.py
from django.shortcuts import render


def base(request):
    return render(request, 'home.html')