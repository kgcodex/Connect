from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status

from .base import BaseAPITest
from .routes import Routes

all_post_url = Routes.ALL_POST.value
post_url = Routes.POST.value


class UserAllPostTest(BaseAPITest):
    def test_get_user_posts(self):
        image = SimpleUploadedFile(
            name="test.png",
            content=open("api/tests/test.png", "rb").read(),
            content_type="image/png",
        )
        payload = {
            "content": "Content Added",
            "media_url": image,
        }

        self.client.post(post_url, payload, format="multipart")

        response = self.client.get(all_post_url, {"username": "testuser"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["username"], "testuser")
