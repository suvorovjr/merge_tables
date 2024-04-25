from django import forms
from django.forms import SelectDateWidget
from merge_files.models import UploadFiles


class StylesMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UploadFilesForm(StylesMixin, forms.ModelForm):
    class Meta:
        model = UploadFiles
        fields = '__all__'
