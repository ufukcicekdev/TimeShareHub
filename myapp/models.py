from django.db import models
import uuid
from django.utils import timezone
from storages.backends.s3boto3 import S3Boto3Storage
# Create your models here.


class CustomS3Boto3Storage(S3Boto3Storage):
    def delete(self, name):
        super().delete(name)

    def save(self, name, content, max_length=None):
        name = self.get_available_name(name)
        
        if self.file_overwrite:
            return super().save(name, content, max_length)
        return super().save(name, content, max_length)

def document_file_path(instance, filename):
    extension = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{extension}'
    return f'timesharehub/{filename}'

class UploadedDocument(models.Model):
    document = models.FileField(upload_to=document_file_path, storage=CustomS3Boto3Storage())
    upload_date = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField()
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)


class UploadCounter(models.Model):
    count = models.PositiveIntegerField(default=0)