from rest_framework.test import APITestCase


class BaseAPITest(APITestCase):
    def setUp(self):
        # Create user
        self.user_data = {
            "email": "test@example.com",
            "username": "testuser",
            "name": "Test User",
            "dob": "1999-01-01",
            "password": "password123",
        }

        self.other_user = {
            "email": "other@example.com",
            "username": "otheruser",
            "name": "Other User",
            "dob": "1999-01-01",
            "password": "password123",
        }

        self.client.post("/api/v1/register/", self.user_data, format="json")
        self.client.post("/api/v1/register/", self.other_user, format="json")

        # Login
        login_res = self.client.post(
            "/api/v1/login/",
            {"email": self.user_data["email"], "password": self.user_data["password"]},
            format="json",
        )
        otherlogin_res = self.client.post(
            "/api/v1/login/",
            {
                "email": self.other_user["email"],
                "password": self.other_user["password"],
            },
            format="json",
        )
        self.access = login_res.data["access"]
        self.other_access = otherlogin_res.data["access"]

        # Store authenticated client
        self.auth_client = self.client
        self.auth_client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access}")
