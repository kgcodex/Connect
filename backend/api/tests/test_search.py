from rest_framework import status

from .base import BaseAPITest
from .routes import Routes

search_url = Routes.SEARCH.value


class SearchTest(BaseAPITest):
    def test_search_user(self):
        response = self.client.get(search_url, {"username": "otheruser"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["username"], "otheruser")

    def test_nonexistant_user(self):
        response = self.client.get(search_url, {"username": "123456"})

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data["error"], "User not found.")

    def test_search_without_username(self):
        response = self.client.get(search_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["error"], "Username is required")
