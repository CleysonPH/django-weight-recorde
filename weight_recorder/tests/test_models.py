import datetime
from django.test import TestCase
from django.contrib.auth.models import User

from weight_recorder.models import Weight


class WeightModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(
            username="TestUser", password="TestPassword")
        Weight.objects.create(
            weight_value=65.1, weight_date=datetime.date.today(), insert_by=test_user)

    def setUp(self):
        self.weight = Weight.objects.get(id=1)

    def test_weight_value_label(self):
        field_label = self.weight._meta.get_field('weight_value').verbose_name
        self.assertEquals(field_label, 'Peso')

    def test_weight_date_label(self):
        field_label = self.weight._meta.get_field('weight_date').verbose_name
        self.assertEquals(field_label, 'Data do registro')

    def test_created_at_label(self):
        field_label = self.weight._meta.get_field('created_at').verbose_name
        self.assertEquals(field_label, 'Data de criação')

    def test_insert_by_label(self):
        field_label = self.weight._meta.get_field('insert_by').verbose_name
        self.assertEquals(field_label, 'Usuário')

    def test_object_name_is_inset_by_username_with_weight_value(self):
        expected_object_name = f'{self.weight.insert_by.username} ({self.weight.weight_value}Kg)'
        self.assertEquals(expected_object_name, str(self.weight))
