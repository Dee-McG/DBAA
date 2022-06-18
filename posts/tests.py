from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post, Reply

class TestViews(TestCase):

    def setUp(self):
        """ Setup test """
        username = "testuser"
        password = "!546hrhtsD" # noqa
        user_model = get_user_model()
        # Create user
        self.user = user_model.objects.create_user(username=username,
                                                   password=password,
                                                   is_superuser=True)
        logged_in = self.client.login(username=username, password=password)
        self.assertTrue(logged_in)
        
        # Create post
        Post.objects.create(user=self.user, title='Hello', body='Test post')

    def test_post_list(self):
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/posts.html')

    def test_post_detail(self):
        post = Post.objects.filter().first()
        response = self.client.get(f'/posts/view/{post.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/view_post.html')


class TestRedirectViews(TestCase):
    def test_post_detail_auth_redirect(self):
        response = self.client.get(f'/posts/view/1/')
        self.assertEqual(response.status_code, 302)

    def test_edit_post_redirect(self):
        response = self.client.get(f'/posts/edit/1/')
        self.assertEqual(response.status_code, 302)

    def test_reply_to_post_redirect(self):
        response = self.client.get(f'/posts/reply/1/')
        self.assertEqual(response.status_code, 302)

    def test_edit_reply_redirect(self):
        response = self.client.get(f'/posts/edit/reply/1/')
        self.assertEqual(response.status_code, 302)