from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase

from apps.app_keys.models import Application


class ApplicationTests(APITestCase):
    def test_create_application(self):
        """
        Ensure we can create a new application object.
        """
        url = reverse('application-list')
        data = {'name': 'test'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Application.objects.count(), 1)
        self.assertEqual(Application.objects.get().name, 'test')
        url = reverse('application-test')
        response = self.client.get(url, headers={'x-api-key': Application.objects.get().key})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'test')



