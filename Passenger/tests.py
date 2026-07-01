from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient


class RegisterEndpointTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register_creates_user_and_profile(self):
        response = self.client.post(
            reverse('register'),
            {
                'username': 'newguest',
                'email': 'newguest@example.com',
                'password': 'StrongPass123',
                'national_code': '1234567890',
            },
            format='json',
        )

        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.data['user']['username'] == 'newguest')
        self.assertTrue(response.data['profile']['NationalCode'] == '1234567890')
