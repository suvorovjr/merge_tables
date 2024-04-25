from django.urls import path
from merge_files.apps import MergefilesConfig
from merge_files.views import IndexView

app_name = MergefilesConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
