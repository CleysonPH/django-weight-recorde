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


class SignUpViewTest(TestCase):
    def setUp(self):
        self.correct_user_data = {
            'username': 'TestUser',
            'password': 'TestPassword',
            'email': 'test@test.com',
            'first_name': 'Test',
            'last_name': 'User'
        }

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/conta/signup')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('accounts:signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('accounts:signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signup.html')

    def test_redirect_for_login_on_correct_user_data(self):
        response = self.client.post(
            reverse('accounts:signup'), self.correct_user_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('accounts:signin'))

    def test_user_is_create_on_corret_user_data(self):
        response = self.client.post(
            reverse('accounts:signup'), self.correct_user_data)
        created_user = User.objects.get(username='TestUser')
        self.assertEqual(created_user.username,
                         self.correct_user_data['username'])
        self.assertEqual(created_user.email, self.correct_user_data['email'])
        self.assertEqual(created_user.first_name,
                         self.correct_user_data['first_name'])
        self.assertEqual(created_user.last_name,
                         self.correct_user_data['last_name'])

    def test_create_user_profile_when_signup(self):
        response = self.client.post(
            reverse('accounts:signup'), self.correct_user_data)
        created_user = User.objects.get(username='TestUser')
        self.assertTrue(created_user.userprofile != None)


class SignOutViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(
            username='TestUser', password='TestPassword')

    def setUp(self):
        self.test_user = {
            'username': 'TestUser',
            'password': 'TestPassword',
        }

    def test_redirect_if_not_logged_in(self):
        response = self.client.get('/conta/signout')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url, f"{reverse('accounts:signin')}?next=/conta/signout")

    def test_view_url_exists_at_desired_location(self):
        login = self.client.login(
            username=self.test_user['username'],
            password=self.test_user['password'],
        )
        response = self.client.get('/conta/signout')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('accounts:signin'))

    def test_view_url_accessible_by_name(self):
        login = self.client.login(
            username=self.test_user['username'],
            password=self.test_user['password'],
        )
        response = self.client.get(reverse('accounts:signout'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('accounts:signin'))

    def test_logout_user(self):
        login = self.client.login(
            username=self.test_user['username'],
            password=self.test_user['password'],
        )
        response = self.client.post(reverse('accounts:signout'), follow=True)
        self.assertFalse(response.context['user'].is_active)
        self.assertFalse(response.context['user'].is_authenticated)


class UserProfileUpdateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(
            username='TestUser', password='TestPassword')
        user_profile = UserProfile.objects.create(
            height=1.75, weight_goal=65.5, user=test_user)

    def setUp(self):
        self.test_user_credentials = {
            'username': 'TestUser',
            'password': 'TestPassword',
        }

        self.test_user = User.objects.get(username='TestUser')

    def test_redirect_if_not_logged_in(self):
        response = self.client.get('/conta/perfil/alterar')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url, f"{reverse('accounts:signin')}?next=/conta/perfil/alterar")

    def test_view_url_exists_at_desired_location(self):
        login = self.client.login(
            username=self.test_user_credentials['username'],
            password=self.test_user_credentials['password'],
        )
        response = self.client.get('/conta/perfil/alterar')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        login = self.client.login(
            username=self.test_user_credentials['username'],
            password=self.test_user_credentials['password'],
        )
        response = self.client.get(reverse('accounts:user_profile_update'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        login = self.client.login(
            username=self.test_user_credentials['username'],
            password=self.test_user_credentials['password'],
        )
        response = self.client.get(reverse('accounts:user_profile_update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'accounts/user_profile_form.html')


class UserProfileUpdateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(
            username='TestUser', password='TestPassword')
        user_profile = UserProfile.objects.create(
            height=1.75, weight_goal=65.5, user=test_user)

    def setUp(self):
        self.test_user_credentials = {
            'username': 'TestUser',
            'password': 'TestPassword',
        }

        self.test_user = User.objects.get(username='TestUser')

    def test_redirect_if_not_logged_in(self):
        response = self.client.get('/conta/senha/alterar')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url, f"{reverse('accounts:signin')}?next=/conta/senha/alterar")

    def test_view_url_exists_at_desired_location(self):
        login = self.client.login(
            username=self.test_user_credentials['username'],
            password=self.test_user_credentials['password'],
        )
        response = self.client.get('/conta/senha/alterar')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        login = self.client.login(
            username=self.test_user_credentials['username'],
            password=self.test_user_credentials['password'],
        )
        response = self.client.get(reverse('accounts:update_password'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        login = self.client.login(
            username=self.test_user_credentials['username'],
            password=self.test_user_credentials['password'],
        )
        response = self.client.get(reverse('accounts:update_password'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'accounts/update_password.html')

    def test_redirects_to_dashboard_on_success(self):
        login = self.client.login(
            username=self.test_user_credentials['username'],
            password=self.test_user_credentials['password'],
        )
        response = self.client.post(reverse('accounts:update_password'), {
                                    'old_password': 'TestPassword', 'new_password1': 'NewTestPassword', 'new_password2': 'NewTestPassword'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('weight_recorder:dashboard'))

    def test_if_password_really_change(self):
        login = self.client.login(
            username=self.test_user_credentials['username'],
            password=self.test_user_credentials['password'],
        )
        old_password = self.test_user.password
        response = self.client.post(reverse('accounts:update_password'), {
                                    'old_password': 'TestPassword', 'new_password1': 'NewTestPassword', 'new_password2': 'NewTestPassword'}, follow=True)
        new_password = response.context['user'].password
        self.assertTrue(old_password != new_password)
