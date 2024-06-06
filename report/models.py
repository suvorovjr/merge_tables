from django.db import models


class ReportFile(models.Model):
    upload_date = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Дата и время загрузки')
    file = models.FileField(upload_to='files', verbose_name='Файл')

    def __str__(self):
        return f'Файл {self.file} загружен {self.upload_date}'

    class Meta:
        verbose_name = 'Загруженный отчет'
        verbose_name_plural = 'Загруженные отчеты'


class Brand(models.Model):
    name = models.CharField(max_length=55, unique=True, verbose_name='Название бренда')

    def __str__(self):
        return f'Бренд - {self.name}'

    class Meta:
        verbose_name = 'бренд'
        verbose_name_plural = 'бренды'
