from django.urls import path, reverse
from .views import upload_document,view_document
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from myapp.sitemap import *

app_name = 'myapp'


sitemaps = {
    'mainLinkSiteMap':MainLinkSiteMap, 
}

urlpatterns = [
    path('', upload_document, name='upload_document'),
    path('document/<uuid:document_uuid>/', view_document, name='view_document'),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    path('robots.txt',TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    
    # Diğer URL tanımları...
]
