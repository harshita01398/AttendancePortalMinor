import os
from django.db.models import Q
from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse, HttpResponse, Http404

from backend.processor.Testing1 import convert

from .models import Record

img_path=""
xls_path=""

def index(request):
    return render(request, 'index.html', None)

# def search_dept(request):
#     query = request.GET.get('query')
#     names = Info.objects.filter(Q(Dept__icontains=query)).values_list('Dept',flat=True).distinct()
#     namesList = []
#     for name in names:
#         namesList.append(str(name))
#     data = {
#         "names": namesList
#     }
#     return JsonResponse(data)

# def search_teacher(request):
#     dept = request.GET.get('dept')
#     query = request.GET.get('query')
#     names = Info.objects.filter(Q(Dept__icontains=dept),Q(TCode__icontains=query)|Q(TeacherName__icontains=query)).values_list('TCode',flat=True).distinct()
#     namesList = []
#     for name in names:
#         obj = Info.objects.filter(TCode=str(name)).first()
#         tcode = getattr(obj, 'TCode')
#         tname = getattr(obj, 'TeacherName')
#         value = str(tname) + " (" + str(tcode) + ")" 
#         namesList.append(str(value))
#     data = {
#         "names": namesList
#     }
#     return JsonResponse(data)

# def search_subject(request):
#     dept = request.GET.get('dept')
#     teacher = request.GET.get('teacher')
#     tcode = teacher[teacher.find("(")+1:teacher.find(")")]
#     query = request.GET.get('query')
#     names = Info.objects.filter(Q(Dept__icontains=dept),Q(TCode=tcode),Q(SubCode__icontains=query)|Q(SubName__icontains=query)).values_list('SubCode',flat=True).distinct()
#     namesList = []
#     for name in names:
#         obj = Info.objects.get(SubCode=str(name))
#         sname = getattr(obj, 'SubName')
#         value = str(sname) + " (" + str(name) + ")" 
#         namesList.append(str(value))
#     data = {
#         "names": namesList
#     }
#     return JsonResponse(data)

def upload(request):
    if request.method == 'POST':
        # subject = request.POST.get('Subject')
        # scode = subject[subject.find("(")+1:subject.find(")")]
        imgFile = request.FILES.get('Image')
        global img_path
        img_path = Record.objects.create(Img=imgFile)
        # img_path = img_obj.url
        print(img_path)

    return JsonResponse({'data':'success'})

def generate_xls(request):
    global xls_path
    xls_path = convert(img_path)
    print(xls_path)
    # rcd1 = Record.objects.filter(Img = img_obj)
    # download_file(xls_path)
    return JsonResponse({'data':'success'})


def download_file(request):
    global xls_path
    if os.path.exists(xls_path):
        with open(xls_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(xls_path)
            return response
    raise Http404


# class CreatePostView(CreateView): # new
#     model = Post
#     form_class = PostForm
#     template_name = 'post.html'
#     success_url = reverse_lazy('index')

