from django.views.generic import CreateView
from merge_files.models import UploadFiles
from merge_files.forms import UploadFilesForm
from django.urls import reverse_lazy


class UploadFilesCreateView(CreateView):
    model = UploadFiles
    form_class = UploadFilesForm
    template_name = 'merge_files/index.html'
    success_url = reverse_lazy('merge_files:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['active_page'] = 'index'
        return context_data
