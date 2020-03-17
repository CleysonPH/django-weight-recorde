import datetime
from django.test import TestCase
from django.contrib.auth.models import User

from weight_recorder.forms import WeightForm


class WeightFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(
            username="TestUser", password="TestPassword")

    def setUp(self):
        self.test_user = User.objects.get(username='TestUser')

    def test_valid_data(self):
        form = WeightForm({
            'weight_value': 65.1,
            'weight_date': datetime.date.today(),
        })

        self.assertTrue(form.is_valid())

        weight = form.save(commit=False)
        weight.insert_by = self.test_user
        weight.save()

        self.assertEqual(weight.weight_value, 65.1)
        self.assertEqual(weight.weight_date, datetime.date.today())

    def test_blank_data(self):
        form = WeightForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'weight_value': ['Este campo é obrigatório.'],
            'weight_date': ['Este campo é obrigatório.'],
        })
