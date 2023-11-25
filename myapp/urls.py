from django.urls import path, reverse
from .views import upload_document,view_document
from django.views.generic import TemplateView

app_name = 'myapp'


urlpatterns = [
    path('', upload_document, name='upload_document'),
    path('document/<uuid:document_uuid>/', view_document, name='view_document'),
    path('robots.txt',TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    # Diğer URL tanımları...
]
