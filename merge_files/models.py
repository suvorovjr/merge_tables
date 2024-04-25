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
