import datetime
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from accounts.models import UserProfile


class SignInViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(
            username='TestUser', password='TestPassword')

    def setUp(self):
        self.correct_user_data = {
            'username': 'TestUser',
            'password': 'TestPassword',
        }

        self.test_user = User.objects.get(username='TestUser')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/conta/signin')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('accounts:signin'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('accounts:signin'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signin.html')

    def test_redirect_for_dashboard_on_correct_user_data(self):
        response = self.client.post(
            reverse('accounts:signin'), self.correct_user_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('weight_recorder:dashboard'))

    def test_login_user_on_correct_user_data(self):
        response = self.client.post(
            reverse('accounts:signin'), self.correct_user_data, follow=True)
        self.assertTrue(response.context['user'].is_active)
        self.assertTrue(response.context['user'].is_authenticated)

    def test_login_correct_user_on_correct_user_data(self):
        response = self.client.post(
            reverse('accounts:signin'), self.correct_user_data, follow=True)
        self.assertEqual(
            response.context['user'].username, self.test_user.username)
