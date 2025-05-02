from django.shortcuts import render
from django.http import JsonResponse
from gps.parsers.wialon_txt_parser import parse_wialon_log_to_geojson
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def map_view(request):
    return render(request, "gps/map.html")

def track_geojson_view(request):
    file_path = os.path.join(BASE_DIR, "gps", "data", "track1.txt")
    if not os.path.isfile(file_path):
        return JsonResponse({"error": "Файл не знайдено"}, status=404)
    geojson = parse_wialon_log_to_geojson(file_path)
    return JsonResponse(geojson, safe=False)
