from django.urls import path, reverse
from .views import upload_document,view_document

app_name = 'myapp'


urlpatterns = [
    path('', upload_document, name='upload_document'),
    path('document/<uuid:document_uuid>/', view_document, name='view_document'),
    # Diğer URL tanımları...
]
