from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload', views.upload, name='upload'),
    path('download', views.download_file, name='download'),
    path('generateXls', views.generate_xls, name='generateXls'),
    path('searchDept', views.search_dept, name='searchDept'),
    path('searchTeacher', views.search_teacher, name='searchTeacher'),
    path('searchSub', views.search_subject, name='searchSub'),
    # path('post/', views.CreatePostView.as_view(), name='add_post')
]