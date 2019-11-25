import os
from django.db.models import Q
from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse, HttpResponse, Http404

from backend.processor.Testing import convert

from .models import Record

img_path=""
xls_path=""

def index(request):
    return render(request, 'index.html', None)

def upload(request):
    if request.method == 'POST':
        imgFile = request.FILES.get('Image')
        global img_path
        img_path = Record.objects.create(Img=imgFile)
        print(img_path)

    return JsonResponse({'data':'success'})

def generate_xls(request):
    global xls_path
    xls_path = convert(img_path)
    print(xls_path)
    return JsonResponse({'data':'success'})


def download_file(request):
    global xls_path
    if os.path.exists(xls_path):
        with open(xls_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(xls_path)
            return response
    raise Http404
