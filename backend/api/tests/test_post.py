from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status

from .base import BaseAPITest
from .routes import Routes

post_url = Routes.POST.value


class PostTest(BaseAPITest):
    def test_add_post(self):
        image = SimpleUploadedFile(
            name="test.png",
            content=open("api/tests/test.png", "rb").read(),
            content_type="image/png",
        )
        payload = {
            "content": "Content Added",
            "media_url": image,
        }

        response = self.client.post(post_url, payload, format="multipart")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["message"], "Post created successfully")

    def test_delete_post(self):
        image = SimpleUploadedFile(
            name="test.png",
            content=open("api/tests/test.png", "rb").read(),
            content_type="image/png",
        )
        payload = {
            "content": "Content Added",
            "media_url": image,
        }
        response = self.client.post(post_url, payload, format="multipart")

        postid = response.data["postid"]

        response = self.client.delete(f"{post_url}?postid={postid}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Post deleted successfully")
