from django.http import JsonResponse
from django.views.generic import CreateView, ListView, DetailView
from .forms import ReportForm
from django.urls import reverse_lazy
from common.mixins import ContextDataMixin
from .models import ReportFile, Brand


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


class ReportDetailView(ContextDataMixin, DetailView):
    model = ReportFile
    template_name = 'report/report_detail.html'
    title = 'Работа с отчетом'


def load_brands(request):
    brands = list(Brand.objects.all().values('id', 'name'))
    return JsonResponse(brands, safe=False)
