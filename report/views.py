from django.shortcuts import render
from django.views.generic import CreateView
from .forms import ReportForm
from django.urls import reverse_lazy
from .models import ReportFile


class ReportCreateView(CreateView):
    form_class = ReportForm
    template_name = 'report/report_form.html'
    success_url = reverse_lazy('merge_files:files_list')
