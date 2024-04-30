from django.views.generic import CreateView, ListView, DetailView, TemplateView, DeleteView
from merge_files.models import UploadFiles, MergedFile
from merge_files.forms import UploadFilesForm
from django.http import HttpResponseRedirect, FileResponse
from django.urls import reverse_lazy
from .tasks import merge_files


class UploadFilesCreateView(CreateView):
    model = UploadFiles
    form_class = UploadFilesForm
    template_name = 'merge_files/index.html'
    success_url = reverse_lazy('merge_files:files_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['active_page'] = 'index'
        return context_data


class UploadFilesListView(ListView):
    model = UploadFiles

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['active_page'] = 'files_list'
        context_data['merged_files_list'] = MergedFile.objects.all()
        return context_data


class UploadFilesDetailView(DetailView):
    model = UploadFiles

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        merge_files.delay(obj.pk)
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
