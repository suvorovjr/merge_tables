from django.views.generic import CreateView, ListView
from .forms import ReportForm
from django.urls import reverse_lazy
from common.mixins import ContextDataMixin
from .models import ReportFile


class ReportCreateView(ContextDataMixin, CreateView):
    form_class = ReportForm
    template_name = 'report/report_form.html'
    success_url = reverse_lazy('merge_files:files_list')
    title = 'Загрузка отчета'
    active_page = 'report_create'


class ReportListView(ContextDataMixin, ListView):
    model = ReportFile
    template_name = 'report/report_list.html'
    title = 'Загруженные отчеты'
    active_page = 'report_list'
