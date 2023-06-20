from django.db import models

from django_quanttide.models import IDField


class ExampleModel(models.Model):
    id = IDField()
