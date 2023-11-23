# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .forms import DocumentUploadForm
from .models import UploadedDocument,UploadCounter
from django.utils import timezone
from django.db.models.signals import post_save
from .tasks import delete_expired_files_s3
from django.http import HttpResponse
from django.dispatch import receiver
from django.db import transaction

def upload_document(request):
    counter_instance = UploadCounter.objects.first()
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            document_instance = form.save(commit=False)
            document_instance.expiration_date = timezone.now() + timezone.timedelta(hours=2)
            document_instance.save()

            document_url = request.build_absolute_uri(f'/document/{document_instance.uuid}/')
            
            return render(request, 'upload/success.html', {'document_url': document_url})
    else:
        form = DocumentUploadForm()
    return render(request, 'upload/upload.html', {'form': form,'upload_count':counter_instance.count })


def view_document(request, document_uuid):
    try:
        document = UploadedDocument.objects.get(uuid=document_uuid)
        return render(request, 'upload/view_document.html', {'document': document})
    except UploadedDocument.DoesNotExist:
        return redirect('/')
        

@receiver(post_save, sender=UploadedDocument)
def increment_upload_counter(sender, instance, created, **kwargs):
    if created:
        with transaction.atomic():
            upload_counter, created = UploadCounter.objects.get_or_create()
            upload_counter.count += 1
            upload_counter.save()


def delete_expired_documents_view(request):
    delete_expired_files_s3.delay() 
    return redirect("/")


def upload_counter_view(request):
    counter_instance = UploadCounter.objects.first()
    print("counter_instance.count",counter_instance.count)
    context = {
        'upload_count': counter_instance.count,
    }
    return render(request, '/', context)