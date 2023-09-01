from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blogtgl.models import Post

class ViewsTestCase(TestCase):
    def setUp(self):
        # Crear un usuario de prueba
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_post_list_view(self):
        # Prueba para la vista 'post_list'
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_list.html')

    def test_post_detail_view(self):
        # Crear un post de prueba
        post = Post.objects.create(title='Test Post', content='This is a test post', author=self.user)

        # Prueba para la vista 'post_detail'
        response = self.client.get(reverse('post_detail', args=[post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_create_post_view(self):
        # Iniciar sesión con el usuario de prueba
        self.client.login(username='testuser', password='testpassword')

        # Prueba para la vista 'create_post'
        response = self.client.get(reverse('create_post'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_post.html')

    def test_repost_post_view(self):
        # Crear un post de prueba
        post = Post.objects.create(title='Test Post', content='This is a test post', author=self.user)

        # Iniciar sesión con el usuario de prueba
        self.client.login(username='testuser', password='testpassword')

        # Prueba para la vista 'repost_post'
        response = self.client.post(reverse('repost_post', args=[post.id]))
        self.assertEqual(response.status_code, 302)  # Redirige después de un repost

    def test_custom_login_view(self):
        # Prueba para la vista 'custom_login'
        response = self.client.get(reverse('custom_login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_custom_logout_view(self):
        # Prueba para la vista 'custom_logout'
        response = self.client.get(reverse('custom_logout'))
        self.assertEqual(response.status_code, 200)  # Redirige después del cierre de sesión

    def test_dashboard_view(self):
        # Iniciar sesión con el usuario de prueba
        self.client.login(username='testuser', password='testpassword')

        # Prueba para la vista 'dashboard'
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')
