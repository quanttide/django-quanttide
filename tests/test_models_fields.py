from django.test import TestCase

from .models import ExampleModel


class IDFieldTestCase(TestCase):
    def test_init(self):
        model_instance = ExampleModel()
        self.assertTrue(model_instance.id)
