from django.db import models


class ReportFile(models.Model):
    upload_date = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Дата и время загрузки')
    file = models.FileField(upload_to='files', verbose_name='Файл')

    class Meta:
        verbose_name = 'Загруженный отчет'
        verbose_name_plural = 'Загруженные отчеты'
