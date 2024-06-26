from celery import shared_task
from django.core.cache import cache
from .services import MergeFiles
from merge_files.models import MergedFile
from django.core.files import File
import os


@shared_task
def merge_files(sanbest_file, market_file):
    merge_file_client = MergeFiles(sanbest_file=sanbest_file, market_file=market_file)
    path_to_merge_file = merge_file_client.merge_files()
    merge_file_instance = MergedFile()
    with open(path_to_merge_file, 'rb') as file:
        django_file = File(file)
        merge_file_instance.merge_file.save(os.path.basename(path_to_merge_file), django_file, save=True)
        merge_file_instance.save()
