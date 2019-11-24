from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase

from .models import Application


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
        print(Application.objects.get().key)
        response = self.client.get(url, HTTP_X_API_KEY=str(Application.objects.get().key))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'test')



