from rest_framework import status
from rest_framework.test import APITestCase

from .routes import Routes


class AuthTests(APITestCase):
    def setUp(self):
        self.register_url = Routes.REGISTER.value
        self.login_url = Routes.LOGIN.value
        self.refresh_url = Routes.REFRESH.value

        self.data = {
            "email": "test@example.com",
            "username": "testuser",
            "name": "Test User",
            "password": "password123",
            "dob": "1990-01-01",
        }

        self.login_details = {
            "email": "test@example.com",
            "password": "password123",
        }

    def test_user_registration(self):
        response = self.client.post(self.register_url, self.data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_old_user_registration(self):
        self.client.post(self.register_url, self.data, format="json")
        response = self.client.post(self.register_url, self.data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data["email"][0], "user with this email already exists."
        )
        self.assertEqual(
            response.data["username"][0], "user with this username already exists."
        )

    def test_dob_gte_18(self):
        response = self.client.post(
            self.register_url, {**self.data, "dob": "2020-01-01"}, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["dob"][0], "User must be at least 18 years old.")

    def test_empty_body(self):
        data = {}
        self.client.post(self.register_url, data, format="json")
        response = self.client.post(self.register_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Login Endpoint
    def test_login(self):
        self.client.post(self.register_url, self.data, format="json")
        response = self.client.post(self.login_url, self.login_details, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("access" in response.data)
        self.assertTrue("refresh" in response.data)

    def test_new_user_login(self):
        response = self.client.post(self.login_url, self.login_details, format="json")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            response.data["detail"],
            "No active account found with the given credentials",
        )

    def test_refresh(self):
        self.client.post(self.register_url, self.data, format="json")
        response = self.client.post(self.login_url, self.login_details, format="json")

        response = self.client.post(
            self.refresh_url, {"refresh": response.data["refresh"]}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("access" in response.data)
