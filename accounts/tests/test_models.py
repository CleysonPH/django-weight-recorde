import datetime
from django.test import TestCase
from django.contrib.auth.models import User

from accounts.models import UserProfile
from weight_recorder.models import Weight


class UserProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(
            username="TestUser", password="TestPassword")
        user_profile = UserProfile.objects.create(
            height=1.75, weight_goal=65.5, user=test_user
        )

        number_of_weights = 10
        for weight_id in range(number_of_weights):
            if weight_id == 9:
                Weight.objects.create(
                    weight_value=61.5,
                    weight_date=datetime.date.today(),
                    insert_by=test_user
                )
            else:
                Weight.objects.create(
                    weight_value=75.5,
                    weight_date=datetime.date.today() - datetime.timedelta(days=1),
                    insert_by=test_user
                )

    def setUp(self):
        self.test_user = User.objects.get(username='TestUser')
        self.test_user_profile = UserProfile.objects.get(id=1)

    def test_profile_image_label(self):
        field_label = self.test_user_profile._meta.get_field(
            'profile_image').verbose_name
        self.assertEqual(field_label, 'Foto de perfil')

    def test_height_label(self):
        field_label = self.test_user_profile._meta.get_field(
            'height').verbose_name
        self.assertEqual(field_label, 'Altura')

    def test_weight_goal_label(self):
        field_label = self.test_user_profile._meta.get_field(
            'weight_goal').verbose_name
        self.assertEqual(field_label, 'Meta de peso')

    def test_user_label(self):
        field_label = self.test_user_profile._meta.get_field(
            'user').verbose_name
        self.assertEqual(field_label, 'Usuário')

    def test_get_imc_calc_with_no_height(self):
        self.test_user_profile.height = 0
        expected_imc = 0
        self.assertEqual(self.test_user_profile.get_imc(), expected_imc)

    def test_get_imc_calc_with_height(self):
        expected_imc = 61.5 / 1.75 ** 2
        self.assertEqual(self.test_user_profile.get_imc(), expected_imc)
