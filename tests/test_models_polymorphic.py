from django.test import TestCase

from tests.models import ParentModel, ChildModel


class PolymorphicModelTestCase(TestCase):
    def setUp(self):
        self.instance = ParentModel.objects.create()
        self.child_instance = ChildModel.objects.create()

    def test_default_type(self):
        # Test that the default type is returned when polymorphic_ctype is None
        self.assertEqual('parentmodel', self.instance.type)

    def test_child_model_type(self):
        print(self.child_instance.__class__.__name__)
        self.assertEqual('childmodel', self.child_instance.type)
