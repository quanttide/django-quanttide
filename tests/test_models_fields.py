import uuid

from django.test import SimpleTestCase, modify_settings
from django.contrib.auth import get_user_model

from django_quanttide.models import (
    IDField, NameField, VerboseNameField, TitleField, DescriptionField,
    TypeField, StatusField, StageField, StageChoices,
    CreatedAtField, UpdatedAtField,
    CreatedByField, UpdatedByField,
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
        self.assertIsNone(field.default)
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
        self.assertIsNone(field.default)
        self.assertTrue(field.blank)
        self.assertTrue(field.null)
        self.assertEqual(field.verbose_name, '标题')

    def test_custom_options(self):
        field = TitleField(max_length=150, blank=False, null=False, verbose_name='关联标题')
        self.assertEqual(field.max_length, 150)
        self.assertFalse(field.blank)
        self.assertFalse(field.null)
        self.assertEqual(field.verbose_name, '关联标题')


class DescriptionFieldTestCase(SimpleTestCase):

    def test_defaults(self):
        field = DescriptionField()
        self.assertEqual(field.default, None)
        self.assertTrue(field.blank)
        self.assertTrue(field.null)
        self.assertEqual(field.verbose_name, '描述')

    def test_custom_options(self):
        field = DescriptionField(default='test', blank=False, null=False, verbose_name='关联描述')
        self.assertEqual(field.default, 'test')
        self.assertFalse(field.blank)
        self.assertFalse(field.null)
        self.assertEqual(field.verbose_name, '关联描述')


class TypeFieldTestCase(SimpleTestCase):

    def test_defaults(self):
        choices = (
            ('book', 'Book'),
            ('movie', 'Movie'),
            ('music', 'Music')
        )
        field = TypeField(choices=choices, default='book')
        self.assertIsInstance(field, TypeField)
        self.assertEqual(field.max_length, 50)
        self.assertEqual(field.choices, choices)
        self.assertEqual(field.default, 'book')
        self.assertEqual(field.verbose_name, '类型')


class StatusFieldTestCase(SimpleTestCase):
    def test_defaults(self):
        choices = (
            ('draft', 'Draft'),
            ('published', 'Published'),
            ('archived', 'Archived')
        )
        field = StatusField(choices=choices, default='draft')
        self.assertIsInstance(field, StatusField)
        self.assertEqual(field.max_length, 50)
        self.assertEqual(field.choices, choices)
        self.assertEqual(field.default, 'draft')
        self.assertEqual(field.verbose_name, '状态')


class StageFieldTestCase(SimpleTestCase):
    def test_defaults(self):
        field = StageField()
        self.assertIsInstance(field, StageField)
        self.assertEqual(field.choices, StageChoices.choices)
        self.assertEqual(field.default, StageChoices.PLANNING)


class CreatedAtFieldTestCase(SimpleTestCase):
    def test_defaults(self):
        """
        假设已知DateTimeField的功能和可靠性，本测试仅测试选项设置，集成到Model类时测试验证业务逻辑。
        """
        field = CreatedAtField()
        self.assertFalse(field.auto_now)
        self.assertTrue(field.auto_now_add)
        self.assertEqual(field.verbose_name, '创建时间')


class UpdatedAtFieldTestCase(SimpleTestCase):
    def test_defaults(self):
        """
        假设已知DateTimeField的功能和可靠性，本测试仅测试选项设置，集成到Model类时测试验证业务逻辑。
        """
        field = UpdatedAtField()
        self.assertTrue(field.auto_now)
        self.assertFalse(field.auto_now_add)
        self.assertEqual(field.verbose_name, '更新时间')


class CreatedByFieldTestCase(SimpleTestCase):
    @modify_settings(INSTALLED_APPS={'append': 'django.contrib.auth'})
    def test_defaults(self):
        created_by_field = CreatedByField()
        self.assertEqual(created_by_field.verbose_name, '创建者')
        self.assertEqual(created_by_field.remote_field.model, get_user_model())
        self.assertTrue(created_by_field.null)


class UpdatedByFieldTestCase(SimpleTestCase):
    @modify_settings(INSTALLED_APPS={'append': 'django.contrib.auth'})
    def test_defaults(self):
        updated_by_field = UpdatedByField()
        self.assertEqual(updated_by_field.verbose_name, '更新者')
        self.assertEqual(updated_by_field.remote_field.model, get_user_model())
        self.assertTrue(updated_by_field.null)
