from django import forms
from .models import UploadedDocument
from django.core.exceptions import ValidationError
from django.forms import FileInput


def validate_file_size(value):

    if not value:
        raise ValidationError('Please select a file.')
    
    filesize = value.size

    if filesize > 500 * 1024 * 1024:  
        raise ValidationError('File size must be under 500 MB.')

class DocumentUploadForm(forms.ModelForm):
    document = forms.FileField(validators=[validate_file_size], 
            widget=forms.ClearableFileInput(attrs={'class': 'custom-file-input'}))

    class Meta:

        model = UploadedDocument
        fields = ['document']

    def clean_document(self):
        document = self.cleaned_data.get('document')
        return document
