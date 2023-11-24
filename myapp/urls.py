from django.urls import path, reverse
from .views import upload_document,view_document
from django.conf.urls import handler404, handler500

app_name = 'myapp'


urlpatterns = [
    path('', upload_document, name='upload_document'),
    path('document/<uuid:document_uuid>/', view_document, name='view_document'),
    # Diğer URL tanımları...
]
handler404 = 'myapp.views.custom_404_view'
handler500 = 'myapp.views.custom_500_view'