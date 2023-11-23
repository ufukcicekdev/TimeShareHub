from django.urls import path, reverse
from .views import upload_document,view_document, delete_expired_documents_view

app_name = 'myapp'


urlpatterns = [
    path('', upload_document, name='upload_document'),
    path('document/<uuid:document_uuid>/', view_document, name='view_document'),
    path('delete_expired_documents/', delete_expired_documents_view, name='delete_expired_documents'),
    # Diğer URL tanımları...
]
