from django.urls import path
from merge_files.apps import MergefilesConfig
from merge_files.views import UploadFilesCreateView

app_name = MergefilesConfig.name

urlpatterns = [
    path('', UploadFilesCreateView.as_view(), name='index'),
]
