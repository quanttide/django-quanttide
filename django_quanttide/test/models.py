from uuid import UUID

from django.db.models import Model
from django.test import TestCase as BaseTestCase


class ModelTestCase(BaseTestCase):
    """
    TestCase for testing Django Model classes.
    """
    model_class: Model = Model
    model_data: dict = {}

    def test_defaults(self):
        # Test initializing a model instance
        model_instance = self.model_class(**self.model_data)
        self.assertIsInstance(model_instance, self.model_class)
        # Test saving a model instance to the database
        model_instance.save()
        # The primary key should be assigned after saving
        # The primary key should be a UUID
        self.assertIsInstance(model_instance.pk, UUID)
        # Suppose the get query method works
        saved_instance = self.model_class.objects.get(pk=model_instance.pk)
        self.assertEqual(model_instance, saved_instance)
        # Return it for more detailed tests
        return model_instance
