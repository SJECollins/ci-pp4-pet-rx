from django.test import TestCase
from .models import Category, Drug
from .forms import PrescrForm


class TestPrescrForm(TestCase):
    """
    Testing prescription form for required fields.
    """

    def setUp(self):
        self.category = Category.objects.create(
            name='Antibiotic'
        )
        self.category.save()
        self.drug = Drug.objects.create(
            name='Amoxiclav',
            dose=12.5,
            measure='mg',
            category=self.category,
            route='PO',
            warnings='None'
        )
        self.drug.save()

    def test_empty_fields(self):
        """
        Empty drug field should return error.
        Frequency and length can be empty.
        """
        form = PrescrForm(data={
            'drug': '',
            'frequency': '',
            'length': '',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['drug'][0], 'This field is required.')

    def test_valid_form(self):
        """
        Form is valid if drug field filled with drug entry.
        Form can be valid if frequency and length not selected.
        """
        form = PrescrForm(data={
            'category': self.drug.category,
            'drug': self.drug,
            'frequency': '',
            'length': '',
        })
        self.assertTrue(form.is_valid())
