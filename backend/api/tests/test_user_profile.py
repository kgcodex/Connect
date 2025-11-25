from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status

from .base import BaseAPITest
from .routes import Routes

profile_url = Routes.PROFILE.value


class UserProfileTests(BaseAPITest):
    def test_get_user_profile(self):
        response = self.client.get(profile_url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], "test@example.com")

    def test_get_other_user_profile(self):
        response = self.client.get(profile_url, {"username": "otheruser"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], "other@example.com")

    def test_get_nonexistent_user_profile(self):
        response = self.client.get(profile_url, {"username": "nouser"})

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patch_user_profile(self):
        image = SimpleUploadedFile(
            name="test.png",
            content=open("api/tests/test.png", "rb").read(),
            content_type="image/png",
        )
        payload = {
            "name": "changed name",
            "bio": "updated bio",
            "profile_pic": image,
            "dob": "2000-01-01",
        }

        response = self.client.patch(profile_url, payload, format="multipart")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "changed name")
        self.assertEqual(response.data["bio"], "updated bio")
        self.assertEqual(response.data["dob"], "2000-01-01")
        self.assertIsNotNone(response.data["profile_pic"])

    def test_patch_with_incorrect_image_format(self):
        payload = {
            "name": "changed name",
            "bio": "updated bio",
            "profile_pic": "image",
            "dob": "2000-01-01",
        }
        response = self.client.patch(profile_url, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_user_profile(self):
        response = self.client.delete(profile_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "User deleted successfully")
