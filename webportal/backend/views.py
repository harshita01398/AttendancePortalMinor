from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from .forms import UploadFileForm


def index(request):
    return render(request, 'index.html', None)

def upload(request):
    if request.method == 'POST':
        print(request.POST)

    return JsonResponse({'data':'success'})
    #     form = UploadFileForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         handle_uploaded_file(request.FILES['file'])
    #         return None
    # else:
    #     form = UploadFileForm()
    # return render(request, 'index.html', {'form': form})
