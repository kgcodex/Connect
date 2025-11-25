from rest_framework import status

from .base import BaseAPITest
from .routes import Routes

following_url = Routes.FOLLOWING.value
follower_url = Routes.FOLLOWER.value


class FollowFunctionalityTest(BaseAPITest):
    def test_follow_a_user(self):
        response = self.client.post(following_url, {"username": "otheruser"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(following_url, {"username": "otheruser"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["message"], "You already follow this user.")

    def test_get_following_list(self):
        self.client.post(following_url, {"username": "otheruser"})

        response = self.client.get(following_url, {"query": "list"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["username"], "otheruser")

    def test_get_following_count(self):
        self.client.post(following_url, {"username": "otheruser"})

        response = self.client.get(following_url, {"query": "count"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_get_follower_list(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.other_access}")
        self.client.post(following_url, {"username": "testuser"})

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access}")
        response = self.client.get(follower_url, {"query": "list"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["username"], "otheruser")

    def test_get_follower_count(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.other_access}")
        self.client.post(following_url, {"username": "testuser"})

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access}")
        response = self.client.get(follower_url, {"query": "count"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_follow_missing_username(self):
        response = self.client.post(following_url, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_follow_invalid_username(self):
        response = self.client.post(following_url, {"username": "doesnotexist"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_following_missing_query(self):
        response = self.client.get(following_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("query parameter is required", response.data["message"])

    def test_following_invalid_query_value(self):
        response = self.client.get(following_url, {"query": "invalid"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["error"], "Only list, count are acceptable.")

    def test_followed_by_invalid_query(self):
        response = self.client.get(follower_url, {"query": "invalid"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["error"], "Only list, count are acceptable.")
