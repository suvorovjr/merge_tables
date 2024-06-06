import os
from django import forms
from .models import ReportFile
from merge_files.forms import StylesMixin


class ReportForm(StylesMixin, forms.ModelForm):

    def clean_file(self):
        cleaned_data = self.cleaned_data['file']
        extension = os.path.splitext(cleaned_data.name)[-1]
        match extension:
            case '.xlsx':
                return cleaned_data
            case _:
                raise forms.ValidationError('Необходимо загрузить файл формата ".xlsx"')

    class Meta:
        model = ReportFile
        fields = '__all__'
