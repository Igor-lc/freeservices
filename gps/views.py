from django.shortcuts import render
from django.http import JsonResponse

def track_api(request):
    track = [
        {"lat": 50.4501, "lng": 30.5234},
        {"lat": 50.4510, "lng": 30.5250},
        {"lat": 50.4520, "lng": 30.5270},
    ]
    return JsonResponse(track, safe=False)

def map_view(request):
    return render(request, 'gps/map.html')