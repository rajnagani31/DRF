from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from .models import UserDetails  # Replace 'yourapp' with your app name


class LoginAPITestCase(APITestCase):
    def setUp(self):
        self.login_url = reverse('login')  # Make sure your login URL is named 'login'

        # Create test user
        self.user = UserDetails.objects.create(
            email="testuser@example.com",
            password=make_password("securepassword"),
            is_delete=False
        )

    def test_login_success(self):
        data = {
            "email": "testuser@example.com",
            "password": "securepassword"
        }
        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('jwt_access_token', response.data['data'])
        self.assertIn('jwt_refresh_token', response.data['data'])
        self.assertEqual(response.data['data']['user_id'], self.user.id)

    def test_login_wrong_password(self):
        data = {
            "email": "testuser@example.com",
            "password": "wrongpassword"
        }
        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['message'], 'plese enter curreact password')

    def test_login_unregistered_email(self):
        data = {
            "email": "nonexistent@example.com",
            "password": "whateverpassword"
        }
        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['message'], 'first register to login')
