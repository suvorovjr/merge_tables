from django.db import models


class UploadFiles(models.Model):
    upload_date = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Дата и время загрузки')
    file1 = models.FileField(upload_to='exel_files/', verbose_name='Файл Sanbest')
    file2 = models.FileField(upload_to='exel_files/', verbose_name='Файл Я.Маркета')

    def __str__(self):
        return f'Файл Sanbest - {self.file1}. Файл Я.Маркета {self.file2}'

    class Meta:
        verbose_name = 'Загруженные файлы'
        verbose_name_plural = 'Загруженные файлы'


class MergedFile(models.Model):
    merge_date = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Дата и время загрузки')
    merge_file = models.FileField(upload_to='merge_files/', verbose_name='Соединенный файл')

    def __str__(self):
        return f'{self.merge_file}'

    class Meta:
        verbose_name = 'Соединенный файл'
        verbose_name_plural = 'Соединенные файлы'
