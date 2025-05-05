from django.contrib.auth.models import User
from django.test import TestCase

from post.models import Post


class TestPost(TestCase):
    def setUp(self):
        self.PASSWORD = "notsecure"
        self.owner = User.objects.create_user(
            "owner", password=self.PASSWORD, first_name="First", last_name="Last"
        )
        self.post = Post.objects.create(
            author=self.owner,
            title="Post Title",
            slug="post-title",
            content="Post Content",
            status="P",
        )
        self.draft_post = Post.objects.create(
            author=self.owner,
            title="Post Title",
            slug="post-title",
            content="Post Content",
            status="D",
        )

    def test_view_post(self):
        response = self.client.get("/post/1/")
        self.assertEqual(200, response.status_code)
        self.assertIn("Post Title", response.text)
        self.assertIn("Post Content", response.text)
        self.assertIn("First Last", response.text)
        self.assertIn(
            self.post.created_at.strftime("%Y-%m-%d %H:%M:%S %Z"), response.text
        )
        self.assertIn(
            self.post.updated_at.strftime("%Y-%m-%d %H:%M:%S %Z"), response.text
        )

    def test_view_post_invalid_post_id(self):
        response = self.client.get("/post/20/")
        self.assertEqual(404, response.status_code)

    def test_view_post_draft_status(self):
        response = self.client.get(f"/post/{self.draft_post.id}/")
        self.assertEqual(404, response.status_code)
