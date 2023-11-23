import os
import boto3
from background_task import background
from myapp.models import UploadedDocument
from django.utils import timezone
from dotenv import load_dotenv

load_dotenv()


AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = os.getenv('AWS_S3_CUSTOM_DOMAIN')
AWS_DEFAULT_ACL = os.getenv('AWS_DEFAULT_ACL')
AWS_S3_REGION_NAME = os.getenv("AWS_S3_REGION_NAME")
AWS_S3_ENDPOINT_URL = os.getenv("AWS_S3_ENDPOINT_URL")

@background(schedule=1)  
def delete_expired_files_s3():
    try:
        now = timezone.now()
        expired_documents = UploadedDocument.objects.filter(expiration_date__lte=now)
        for document in expired_documents:
            file_path = document.document.name 
            print("file_path",file_path)

            document.document.storage.delete(file_path) 

            document.delete()

            print(f"Dosya silindi: {file_path}")
    except Exception as e:
        print(f"Dosya silme hatası: {e}")

# Kullanım
delete_expired_files_s3()
