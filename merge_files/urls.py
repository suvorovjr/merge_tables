from django.urls import path
from merge_files.apps import MergefilesConfig
from merge_files.views import UploadFilesCreateView, UploadFilesListView, UploadFilesDetailView, PageIngo, \
    FileDownloadView, UploadFilesDeleteView, MergedFileDeleteView

app_name = MergefilesConfig.name

urlpatterns = [
    path('', UploadFilesCreateView.as_view(), name='index'),
    path('files_list', UploadFilesListView.as_view(), name='files_list'),
    path('merge-files/<int:pk>/', UploadFilesDetailView.as_view(), name='merge_files'),
    path('download-file/<int:pk>/', FileDownloadView.as_view(), name='download_file'),
    path('page-info/', PageIngo.as_view(), name='page-info'),
    path('uploads-delete/<int:pk>', UploadFilesDeleteView.as_view(), name='delete_upload_files'),
    path('merge-delete/<int:pk>', MergedFileDeleteView.as_view(), name='delete_merge_file'),
]
