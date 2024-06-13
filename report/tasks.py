from celery import shared_task
from .services import MakeReport
from .models import ChangeReport
from django.core.files import File
import os


@shared_task
def merge_files(file_path, data):
    report_client = MakeReport(file_path=file_path, data=data)
    report_client.change_df()
    report_client.set_difference()
    path_to_report = report_client.save_to_excel()
    change_report_instance = ChangeReport()
    with open(path_to_report, 'rb') as file:
        django_file = File(file)
        change_report_instance.file.save(os.path.basename(path_to_report), django_file, save=True)
        change_report_instance.save()
