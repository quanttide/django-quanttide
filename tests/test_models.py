import uuid
import datetime

from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

from tests.models import ExampleModel


class ExampleModelTestCase(TestCase):
    def setUp(self):
        self.example = ExampleModel.objects.create(
            name='example',
            verbose_name='example model',
            title='Example Model',
            description='An example model',
            type='book',
            status='draft',
            stage=1
        )

    def test_defaults(self):
        example = self.example
        self.assertEqual(example.name, 'example')
        self.assertEqual(example.verbose_name, 'example model')
        self.assertEqual(example.title, 'Example Model')
        self.assertEqual(example.description, 'An example model')
        self.assertEqual(example.type, 'book')
        self.assertEqual(example.status, 'draft')
        self.assertEqual(example.stage, 1)
        self.assertIsInstance(example.id, uuid.UUID)
        self.assertIsInstance(example.created_at, datetime.datetime)
        self.assertIsInstance(example.updated_at, datetime.datetime)

    def test_name_unique(self):
        example2 = ExampleModel(name='example', verbose_name='example model 2')
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
