from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status

from .base import BaseAPITest
from .routes import Routes

post_url = Routes.POST.value
feed_url = Routes.FEED.value
following_url = Routes.FOLLOWING.value


class FeedTest(BaseAPITest):
    def test_user_feed(self):
        image = SimpleUploadedFile(
            name="test.png",
            content=open("api/tests/test.png", "rb").read(),
            content_type="image/png",
        )
        payload = {
            "content": "Content Added",
            "media_url": image,
        }
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.other_access}")
        self.client.post(post_url, payload, format="multipart")

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access}")
        self.client.post(following_url, {"username": "otheruser"})
        response = self.client.get(feed_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["username"], "otheruser")
