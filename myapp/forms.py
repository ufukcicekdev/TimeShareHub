from django import forms
from .models import UploadedDocument
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField

def validate_file_size(value):
    if not value:
        raise ValidationError('Please select a file.')

    filesize = value.size

    if filesize > 50 * 1024 * 1024:  
        raise ValidationError('File size must be under 50 MB.')

class DocumentUploadForm(forms.ModelForm):
    document = forms.FileField(validators=[validate_file_size], widget=forms.ClearableFileInput(attrs={'class': 'custom-file-input'}))
    captcha = CaptchaField()

    def clean(self):
        cleaned_data = super().clean()
        document = cleaned_data.get('document')

        if document:
            validate_file_size(document)

        return cleaned_data

    class Meta:
        model = UploadedDocument
        fields = ['document', 'captcha']
