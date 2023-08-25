from django.db.models import Model
from django.urls import reverse
from rest_framework import status
from rest_framework.serializers import BaseSerializer
from rest_framework.test import APITestCase as BaseAPITestCase


class ViewSetAPITestCase(BaseAPITestCase):
    """
    Testing APIs provided by ViewSet and Router classes.
    """

    app_name: str = ''
    router_basename: str = ''
    model_class: Model = Model
    serializer_class: BaseSerializer = BaseSerializer
    lookup_kwargs: dict = {}

    @classmethod
    def setUpTestData(cls):
        cls.model_instance = cls.model_class.objects.get(**cls.lookup_kwargs)
        cls.list_url = reverse(f'{cls.app_name}:{cls.router_basename}-list')
        cls.detail_url = reverse(f'{cls.app_name}:{cls.router_basename}-detail',
                                 kwargs=cls.lookup_kwargs)

    def test_list(self):
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail(self):
        response = self.client.get(self.detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
