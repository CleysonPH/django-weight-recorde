import datetime
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from weight_recorder.models import Weight


class DashboardViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(
            username="TestUser", password="TestPassword")

        another_test_user = User.objects.create_user(
            username="AnotherTestUser", password="AnotherTestPassword")

        number_of_weights = 10
        for _ in range(number_of_weights):
            Weight.objects.create(
                weight_value=65.1, weight_date=datetime.date.today(), insert_by=test_user)

        for _ in range(number_of_weights):
            Weight.objects.create(
                weight_value=65.1, weight_date=datetime.date.today(), insert_by=another_test_user)

    def setUp(self):
        self.test_user = {
            'username': 'TestUser',
            'password': 'TestPassword',
        }

    def test_redirect_if_not_logged_in(self):
        response = self.client.get('/dashboard')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/conta/signin'))

    def test_view_url_exists_at_desired_location(self):
        login = self.client.login(
            username=self.test_user['username'],
            password=self.test_user['password'],
        )
        response = self.client.get('/dashboard')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        login = self.client.login(
            username=self.test_user['username'],
            password=self.test_user['password'],
        )
        response = self.client.get(reverse('weight_recorder:dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        login = self.client.login(
            username=self.test_user['username'],
            password=self.test_user['password'],
        )
        response = self.client.get(reverse('weight_recorder:dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'weight_recorder/dashboard.html')

    def test_list_all_weigths(self):
        login = self.client.login(
            username=self.test_user['username'],
            password=self.test_user['password'],
        )
        response = self.client.get(reverse('weight_recorder:dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['weight_list']) == 10)

    def test_only_weights_of_the_logged_user_is_show(self):
        login = self.client.login(
            username=self.test_user['username'],
            password=self.test_user['password'],
        )
        response = self.client.get(reverse('weight_recorder:dashboard'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.context['user']), 'TestUser')
        self.assertTrue('weight_list' in response.context)

        weights = Weight.objects.filter(insert_by=response.context['user'])

        for weight in weights:
            self.assertEqual(response.context['user'], weight.insert_by)


class WeightCreateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(
            username="TestUser", password="TestPassword")

        another_test_user = User.objects.create_user(
            username="AnotherTestUser", password="AnotherTestPassword")

        number_of_weights = 10
        for _ in range(number_of_weights):
            Weight.objects.create(
                weight_value=65.1, weight_date=datetime.date.today(), insert_by=test_user)

        for _ in range(number_of_weights):
            Weight.objects.create(
                weight_value=65.1, weight_date=datetime.date.today(), insert_by=another_test_user)

    def setUp(self):
        self.test_user = {
            'username': 'TestUser',
            'password': 'TestPassword',
        }

    def test_redirect_if_not_logged_in(self):
        response = self.client.get('/peso/adicionar')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/conta/signin'))

    def test_view_url_exists_at_desired_location(self):
        login = self.client.login(
            username=self.test_user['username'],
            password=self.test_user['password'],
        )
        response = self.client.get('/peso/adicionar')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        login = self.client.login(
            username=self.test_user['username'],
            password=self.test_user['password'],
        )
        response = self.client.get(reverse('weight_recorder:weight_create'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        login = self.client.login(
            username=self.test_user['username'],
            password=self.test_user['password'],
        )
        response = self.client.get(reverse('weight_recorder:weight_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'weight_recorder/weight_form.html')


class WeightEditViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(
            username="TestUser", password="TestPassword")

        another_test_user = User.objects.create_user(
            username="AnotherTestUser", password="AnotherTestPassword")

        number_of_weights = 10
        for _ in range(number_of_weights):
            Weight.objects.create(
                weight_value=65.1, weight_date=datetime.date.today(), insert_by=test_user)

        for _ in range(number_of_weights):
            Weight.objects.create(
                weight_value=65.1, weight_date=datetime.date.today(), insert_by=another_test_user)

    def setUp(self):
        self.test_user = {
            'username': 'TestUser',
            'password': 'TestPassword',
        }

    def test_redirect_if_not_logged_in(self):
        response = self.client.get('/peso/1/editar')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/conta/signin'))

    def test_view_url_exists_at_desired_location(self):
        login = self.client.login(
            username=self.test_user['username'],
            password=self.test_user['password'],
        )
        response = self.client.get('/peso/1/editar')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        login = self.client.login(
            username=self.test_user['username'],
            password=self.test_user['password'],
        )
        response = self.client.get(
            reverse('weight_recorder:weight_edit', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        login = self.client.login(
            username=self.test_user['username'],
            password=self.test_user['password'],
        )
        response = self.client.get(
            reverse('weight_recorder:weight_edit', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'weight_recorder/weight_form.html')

    def test_if_not_found_for_edit_a_weight_insert_by_another_user(self):
        login = self.client.login(
            username=self.test_user['username'],
            password=self.test_user['password'],
        )
        response = self.client.get(
            reverse('weight_recorder:weight_edit', kwargs={'pk': 15}))
        self.assertEqual(response.status_code, 404)


class WeightRemoveViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(
            username="TestUser", password="TestPassword")

        another_test_user = User.objects.create_user(
            username="AnotherTestUser", password="AnotherTestPassword")

        number_of_weights = 10
        for _ in range(number_of_weights):
            Weight.objects.create(
                weight_value=65.1, weight_date=datetime.date.today(), insert_by=test_user)

        for _ in range(number_of_weights):
            Weight.objects.create(
                weight_value=65.1, weight_date=datetime.date.today(), insert_by=another_test_user)

    def setUp(self):
        self.test_user = {
            'username': 'TestUser',
            'password': 'TestPassword',
        }

    def test_redirect_if_not_logged_in(self):
        response = self.client.get('/peso/1/apagar')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/conta/signin'))

    def test_view_url_exists_at_desired_location(self):
        login = self.client.login(
            username=self.test_user['username'],
            password=self.test_user['password'],
        )
        response = self.client.get('/peso/1/apagar')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('weight_recorder:dashboard'))

    def test_view_url_accessible_by_name(self):
        login = self.client.login(
            username=self.test_user['username'],
            password=self.test_user['password'],
        )
        response = self.client.get(
            reverse('weight_recorder:weight_delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('weight_recorder:dashboard'))

    def test_if_not_found_for_remove_a_weight_insert_by_another_user(self):
        login = self.client.login(
            username=self.test_user['username'],
            password=self.test_user['password'],
        )
        response = self.client.get(
            reverse('weight_recorder:weight_delete', kwargs={'pk': 15}))
        self.assertEqual(response.status_code, 404)
