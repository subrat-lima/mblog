from django.contrib.auth.models import User
from django.test import TestCase

from posts.models import Post


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
        self.post_2 = Post.objects.create(
            author=self.owner,
            title="Post Title 2",
            slug="post-title-2",
            content="Post Content 2",
            status="P",
        )
        self.post_3 = Post.objects.create(
            author=self.owner,
            title="Post Title 3",
            slug="post-title-3",
            content="""## Sample **html** content\n\n- list item 1\n- list item 2""",
            status="P",
        )
        self.draft_post = Post.objects.create(
            author=self.owner,
            title="Post Title Draft",
            slug="post-title-draft",
            content="Post Content Draft",
            status="D",
        )

    def test_view_post(self):
        # normal post
        response = self.client.get("/posts/1/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Post Title")
        self.assertContains(response, "Post Content")
        self.assertContains(response, "First Last")
        self.assertContains(
            response, self.post.created_at.strftime("%Y-%m-%d %H:%M:%S %Z")
        )
        self.assertContains(
            response, self.post.updated_at.strftime("%Y-%m-%d %H:%M:%S %Z")
        )
        # markdown post
        response = self.client.get(f"/posts/{self.post_3.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Post Title 3")
        self.assertContains(
            response, "<h2>Sample <strong>html</strong> content</h2>", html=True
        )
        self.assertContains(response, "<li>list item 1</li>", html=True)
        self.assertContains(response, "<li>list item 2</li>", html=True)
        self.assertContains(response, "First Last")
        self.assertContains(
            response, self.post_3.created_at.strftime("%Y-%m-%d %H:%M:%S %Z")
        )
        self.assertContains(
            response, self.post_3.updated_at.strftime("%Y-%m-%d %H:%M:%S %Z")
        )

    def test_view_post_invalid_post_id(self):
        response = self.client.get("/posts/20/")
        self.assertEqual(response.status_code, 404)

    def test_view_post_draft_status(self):
        response = self.client.get(f"/posts/{self.draft_post.id}/")
        self.assertEqual(response.status_code, 404)

    def test_view_posts(self):
        response = self.client.get("/posts/")
        self.assertEqual(response.status_code, 200)
        # post 1
        self.assertContains(response, "Post Title")
        self.assertContains(response, self.post.created_at.strftime("%Y-%m-%d"))
        # post 2
        self.assertContains(response, "Post Title 2")
        self.assertContains(
            response,
            self.post_2.created_at.strftime("%Y-%m-%d"),
        )
        # draft post
        self.assertNotContains(response, "Post Title Draft")
