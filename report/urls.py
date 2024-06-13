from django.urls import path
from .apps import ReportConfig
from .views import ReportCreateView, ReportListView, ReportDetailView, load_brands, ReportDownloadView

app_name = ReportConfig.name

urlpatterns = [
    path('', ReportCreateView.as_view(), name='create'),
    path('list/', ReportListView.as_view(), name='list'),
    path('detail/<int:pk>/', ReportDetailView.as_view(), name='detail'),
    path('api/brands/', load_brands, name='load_brands'),
    path('download-report/<int:pk>/', ReportDownloadView.as_view(), name='download_report'),
]
