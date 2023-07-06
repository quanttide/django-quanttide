import uuid
import datetime

from django.test import TestCase
from django.db.utils import IntegrityError

from tests.models import (
    ExampleModel,
    ExamplePolymorphicModel, ChildModel
)


class ModelTestCase(TestCase):
    def setUp(self):
        self.example = ExampleModel.objects.create(
            name='example',
            verbose_name='example instance',
            title='Example Model',
            description='An example instance',
            type='book',
            status='draft',
            stage=1
        )

    def test_defaults(self):
        example = self.example
        self.assertEqual(example.name, 'example')
        self.assertEqual(example.verbose_name, 'example instance')
        self.assertEqual(example.title, 'Example Model')
        self.assertEqual(example.description, 'An example instance')
        self.assertEqual(example.type, 'book')
        self.assertEqual(example.status, 'draft')
        self.assertEqual(example.stage, 1)
        self.assertIsInstance(example.id, uuid.UUID)
        self.assertIsInstance(example.created_at, datetime.datetime)
        self.assertIsInstance(example.updated_at, datetime.datetime)

    def test_name_unique(self):
        example2 = ExampleModel(name='example', verbose_name='example instance 2')
        with self.assertRaises(IntegrityError):
            example2.save()

    def test_created_at(self):
        example = self.example
        self.assertIsInstance(example.created_at, datetime.datetime)
        self.assertLessEqual(datetime.datetime.now() - example.created_at, datetime.timedelta(seconds=1))

    def test_updated_at(self):
        example = self.example
        self.assertIsInstance(example.updated_at, datetime.datetime)
        self.assertLessEqual(datetime.datetime.now() - example.updated_at, datetime.timedelta(seconds=1))
        example.name = 'updated-example'
        example.save()
        self.assertLessEqual(example.updated_at - example.created_at, datetime.timedelta(seconds=1))


class PolymorphicModelTestCase(TestCase):
    def setUp(self):
        self.instance = ExamplePolymorphicModel.objects.create()
        self.child_instance = ChildModel.objects.create()

    def test_default_type(self):
        # Test that the default type is returned when polymorphic_ctype is None
        self.assertEqual('default', self.instance.type)

    def test_child_model_type(self):
        print(self.child_instance.__class__.__name__)
        self.assertEqual('child_model', self.child_instance.type)
