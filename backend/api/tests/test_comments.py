from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status

from .base import BaseAPITest
from .routes import Routes

post_url = Routes.POST.value
comment_url = Routes.COMMENT.value


class CommentTest(BaseAPITest):
    def test_add_comment(self):
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

        payload = {
            "post": postid,
            "content": "Post Content",
        }

        response = self.client.post(comment_url, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["message"], "Comment added successfully")

    def test_get_all_comments(self):
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

        payload = {
            "post": postid,
            "content": "Post Content",
        }
        self.client.post(comment_url, payload)

        response = self.client.get(comment_url, {"postid": postid})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["username"], "testuser")
