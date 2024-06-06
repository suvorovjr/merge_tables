from django.urls import path
from .apps import ReportConfig
from .views import ReportCreateView, ReportListView, ReportDetailView

app_name = ReportConfig.name

urlpatterns = [
    path('', ReportCreateView.as_view(), name='create'),
    path('list/', ReportListView.as_view(), name='list'),
    path('detail/<int:pk>/', ReportDetailView.as_view(), name='detail')
]
