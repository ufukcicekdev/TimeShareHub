# Generated by Django 4.2.7 on 2023-11-23 20:26

from django.db import migrations, models
import myapp.models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UploadCounter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("count", models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="UploadedDocument",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "document",
                    models.FileField(
                        storage=myapp.models.CustomS3Boto3Storage(),
                        upload_to=myapp.models.document_file_path,
                    ),
                ),
                ("upload_date", models.DateTimeField(auto_now_add=True)),
                ("expiration_date", models.DateTimeField()),
                (
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
            ],
        ),
    ]
