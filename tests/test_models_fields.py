import uuid
from django.test import SimpleTestCase
from django_quanttide.models import (
    IDField, NameField, VerboseNameField, TitleField
)


class IDFieldTestCase(SimpleTestCase):
    def test_defaults(self):
        field = IDField()
        self.assertTrue(field.primary_key)
        self.assertFalse(field.editable)
        self.assertEqual(field.verbose_name, 'ID')
        self.assertIsInstance(field.default(), uuid.UUID)

    def test_custom_options(self):
        field = IDField(primary_key=False, verbose_name='关联ID')
        self.assertFalse(field.primary_key)
        self.assertTrue(field.editable)
        self.assertEqual(field.verbose_name, '关联ID')
        self.assertIsInstance(field.default(), uuid.UUID)


class NameFieldTestCase(SimpleTestCase):
    def test_defaults(self):
        field = NameField()
        self.assertEqual(field.max_length, 100)
        self.assertTrue(field.unique)
        self.assertEqual(field.verbose_name, '标识')

    def test_custom_options(self):
        field = NameField(max_length=150, unique=True, verbose_name='关联标识')
        self.assertEqual(field.max_length, 150)
        self.assertTrue(field.unique)
        self.assertEqual(field.verbose_name, '关联标识')


class VerboseNameFieldTestCase(SimpleTestCase):

    def test_defaults(self):
        field = VerboseNameField()
        self.assertEqual(field.max_length, 100)
        self.assertTrue(field.blank)
        self.assertTrue(field.null)
        self.assertEqual(field.verbose_name, '标题')

    def test_custom_options(self):
        field = VerboseNameField(max_length=150, blank=False, null=False, verbose_name='关联标题')
        self.assertEqual(field.max_length, 150)
        self.assertFalse(field.blank)
        self.assertFalse(field.null)
        self.assertEqual(field.verbose_name, '关联标题')


class TitleFieldTestCase(SimpleTestCase):

    def test_defaults(self):
        field = TitleField()
        self.assertEqual(field.max_length, 255)
        self.assertTrue(field.blank)
        self.assertTrue(field.null)
        self.assertEqual(field.verbose_name, '标题')

    def test_custom_options(self):
        field = TitleField(max_length=150, blank=False, null=False, verbose_name='关联标题')
        self.assertEqual(field.max_length, 150)
        self.assertFalse(field.blank)
        self.assertFalse(field.null)
        self.assertEqual(field.verbose_name, '关联标题')
