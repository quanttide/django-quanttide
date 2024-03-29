# Generated by Django 4.2.3 on 2023-08-24 10:10

from django.db import migrations
import django_quanttide.models.fields
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Member",
            fields=[
                (
                    "id",
                    django_quanttide.models.fields.IDField(
                        blank=False,
                        default=uuid.uuid4,
                        editable=False,
                        null=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "org_user_id",
                    django_quanttide.models.fields.IDField(
                        blank=True,
                        default=None,
                        editable=True,
                        null=True,
                        primary_key=False,
                        verbose_name="组织用户ID",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
