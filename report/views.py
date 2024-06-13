import json
from json.decoder import JSONDecodeError
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
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


@method_decorator(csrf_exempt, name='dispatch')
class ProductSubmitView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            if len(data) == 0:
                raise JSONDecodeError(msg='Пустой список!', doc='', pos=0)
            return JsonResponse({'status': 'success'})
        except JSONDecodeError as e:
            return JsonResponse({'status': 'error', 'message': e.msg})
