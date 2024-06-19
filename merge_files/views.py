from django.views.generic import CreateView, ListView, DetailView, TemplateView, DeleteView
from merge_files.models import UploadFiles, MergedFile
from merge_files.forms import UploadFilesForm
from django.http import HttpResponseRedirect, FileResponse
from django.urls import reverse_lazy
from .tasks import merge_files
from common.mixins import ContextDataMixin


class UploadFilesCreateView(ContextDataMixin, CreateView):
    form_class = UploadFilesForm
    template_name = 'merge_files/index.html'
    success_url = reverse_lazy('merge_files:files_list')
    title = 'Загрузка файлов для сравнения'
    active_page = 'index'


class UploadFilesListView(ContextDataMixin, ListView):
    model = UploadFiles
    title = 'Список файлов'
    active_page = 'files_list'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        context_data['additional_object_list'] = MergedFile.objects.all()
        return context_data


class UploadFilesDetailView(DetailView):
    model = UploadFiles

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        san_file = obj.san_file.path
        market_file = obj.market_file.path
        merge_files.delay(san_file, market_file)
        return HttpResponseRedirect('/page-info/')


class UploadFilesDeleteView(DeleteView):
    model = UploadFiles
    success_url = reverse_lazy('merge_files:files_list')


class MergedFileDeleteView(DeleteView):
    model = MergedFile
    success_url = reverse_lazy('merge_files:files_list')

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.merge_file:
            obj.merge_file.delete(save=False)
        response = super(MergedFileDeleteView, self).delete(request, *args, **kwargs)
        obj.delete()
        return response


class FileDownloadView(DetailView):
    model = MergedFile

    def get(self, request, *args, **kwargs):
        file_object = self.get_object()
        response = FileResponse(file_object.merge_file.open(), as_attachment=True, filename=file_object.merge_file.name)
        return response


class PageIngo(TemplateView):
    template_name = 'merge_files/info.html'
