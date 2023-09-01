from django.test import TestCase
from django.contrib.auth import get_user_model
from blogtgl.models import Post, Comment, Repost

class PostModelTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpassword"
        )
        self.post = Post.objects.create(
            title="Test Post",
            content="This is a test post.",
            author=self.user
        )

    def test_post_title(self):
        self.assertEqual(self.post.title, "Test Post")

    def test_post_content(self):
        self.assertEqual(self.post.content, "This is a test post.")

    def test_post_author(self):
        self.assertEqual(self.post.author, self.user)

class CommentModelTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpassword"
        )
        self.post = Post.objects.create(
            title="Test Post",
            content="This is a test post.",
            author=self.user
        )
        self.comment = Comment.objects.create(
            user=self.user,
            post=self.post,
            text="This is a test comment."
        )

    def test_comment_text(self):
        self.assertEqual(self.comment.text, "This is a test comment.")

    def test_comment_user(self):
        self.assertEqual(self.comment.user, self.user)

    def test_comment_post(self):
        self.assertEqual(self.comment.post, self.post)

class RepostModelTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpassword"
        )
        self.post = Post.objects.create(
            title="Test Post",
            content="This is a test post.",
            author=self.user
        )
        self.repost = Repost.objects.create(
            user=self.user,
            post=self.post
        )

    def test_repost_user(self):
        self.assertEqual(self.repost.user, self.user)

    def test_repost_post(self):
        self.assertEqual(self.repost.post, self.post)
