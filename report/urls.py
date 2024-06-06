from django.urls import path
from .apps import ReportConfig
from .views import ReportCreateView

app_name = ReportConfig.name

urlpatterns = [
    path('', ReportCreateView.as_view(), name='create')
]
