from django.http import FileResponse, Http404, HttpResponse
from django.shortcuts import render
from django.conf import settings
import os
from django.views.decorators.http import require_POST



def homepage(request):
    return render(request, 'downloader/home.html')


@require_POST
def download_youtube_downloader(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'downloads', 'FreeYouTubeDownloaderSetup.exe')
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True)
    else:
        raise Http404("Файл не знайдено.")

