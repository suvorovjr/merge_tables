from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete


# class AbstractFile(models.Model):
#     upload_date = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Дата и время загрузки')
#     file = models.FileField(upload_to='files', verbose_name='Файл')
#
#     def __str__(self):
#         return f'Файл {self.file} загружен {self.upload_date}'
#
#     class Meta:
#         abstract = True


class UploadFiles(models.Model):
    upload_date = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Дата и время загрузки')
    san_file = models.FileField(upload_to='exel_files/', verbose_name='Файл Sanbest')
    market_file = models.FileField(upload_to='exel_files/', verbose_name='Файл Я.Маркета')

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


@receiver(post_delete)
def delete_attached_file(sender, instance, **kwargs):
    """
    После удаления экземпляра MyModel удаляет файл из файловой системы.
    """
    if sender == UploadFiles:
        if instance.san_file:
            instance.san_file.delete(save=False)
        if instance.market_file:
            instance.market_file.delete(save=False)
    elif sender == MergedFile:
        if instance.merge_file:
            instance.merge_file.delete(save=False)
