import uuid
from django.test import TestCase
from django_quanttide.models import IDField


class IDFieldTestCase(TestCase):
    def test_defaults(self):
        field = IDField()
        self.assertTrue(field.primary_key)
        self.assertFalse(field.editable)
        self.assertEqual(field.verbose_name, 'ID')
        self.assertIsInstance(field.default(), uuid.UUID)

    def test_custom_options(self):
        field = IDField(primary_key=False, verbose_name='Custom ID')
        self.assertFalse(field.primary_key)
        self.assertTrue(field.editable)
        self.assertEqual(field.verbose_name, 'Custom ID')
        self.assertIsInstance(field.default(), uuid.UUID)
