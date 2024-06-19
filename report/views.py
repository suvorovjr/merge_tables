import json
from json.decoder import JSONDecodeError
from django.http import JsonResponse, FileResponse
from django.utils.decorators import method_decorator
from .tasks import change_report
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView, DetailView
from .forms import ReportForm
from django.urls import reverse_lazy
from common.mixins import ContextDataMixin
from .models import ReportFile, Brand, ChangeReport


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

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        context_data['additional_object_list'] = ChangeReport.objects.all()
        return context_data


@method_decorator(csrf_exempt, name='dispatch')
class ReportDetailView(ContextDataMixin, DetailView):
    model = ReportFile
    template_name = 'report/report_detail.html'
    title = 'Работа с отчетом'

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        try:
            data = json.loads(request.body)
            if len(data) == 0:
                raise JSONDecodeError(msg='Пустой список!', doc='', pos=0)
            change_report.delay(obj.file.path, data)
            return JsonResponse({'status': 'success'})
        except JSONDecodeError as e:
            return JsonResponse({'status': 'error', 'message': e.msg})


class ReportDownloadView(DetailView):
    model = ChangeReport

    def get(self, request, *args, **kwargs):
        file_object = self.get_object()
        response = FileResponse(file_object.file.open(), as_attachment=True, filename=file_object.file.name)
        return response


def load_brands(request):
    brands = list(Brand.objects.all().values('id', 'name'))
    return JsonResponse(brands, safe=False)
