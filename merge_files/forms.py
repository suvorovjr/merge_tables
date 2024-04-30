from django import forms
from merge_files.models import UploadFiles
import os


class StylesMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UploadFilesForm(StylesMixin, forms.ModelForm):
    class Meta:
        model = UploadFiles
        fields = '__all__'

    def clean_san_file(self):
        cleaned_data = self.cleaned_data['san_file']
        extension = os.path.splitext(cleaned_data.name)[-1]
        if extension != '.csv':
            raise forms.ValidationError('Неподдерживаемый формат файла. Для файла Sanbest разрешен только CSV формат.')
        return cleaned_data

    def clean_market_file(self):
        cleaned_data = self.cleaned_data['market_file']
        extension = os.path.splitext(cleaned_data.name)[-1]
        if extension != '.xlsx':
            raise forms.ValidationError(
                'Неподдерживаемый формат файла. Для файла Я.Маркета разрешен только XLSX формат.')
        return cleaned_data
