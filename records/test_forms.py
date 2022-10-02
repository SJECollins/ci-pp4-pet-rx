from django.test import TestCase
from .forms import RecordForm, WeightForm, NoteForm


class TestRecordForm(TestCase):
    """
    Testing record form for required fields.
    """
    def test_empty_fields(self):
        """
        Empty fields should return error.
        """
        form = RecordForm(data={
            'name': '',
            'surname': '',
            'date_of_birth': '',
            'species': '',
            'breed': '',
            'sex': '',
            'weight': ''
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'][0], 'This field is required.')
        self.assertEqual(form.errors['surname'][0], 'This field is required.')
        self.assertEqual(form.errors['date_of_birth'][0], 'This field is required.')
        self.assertEqual(form.errors['species'][0], 'This field is required.')
        self.assertEqual(form.errors['breed'][0], 'This field is required.')
        self.assertEqual(form.errors['sex'][0], 'This field is required.')
        self.assertEqual(form.errors['weight'][0], 'This field is required.')

    def test_valid_form(self):
        """
        Form is valid if all fields filled.
        """
        form = RecordForm(data={
            'name': 'Bob',
            'surname': 'Bobberson',
            'date_of_birth': '12/12/2012',
            'species': 'Canine',
            'breed': 'JRT',
            'sex': 'MN',
            'weight': 12.5
            })
        self.assertTrue(form.is_valid())


class TestWeightForm(TestCase):
    """
    Testing weight form for required fields.
    """
    def test_empty_fields(self):
        form = WeightForm(data={
            'weight': '',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['weight'][0], 'This field is required.')

    def test_valid_form(self):
        form = WeightForm(data={
            'weight': 30
        })
        self.assertTrue(form.is_valid())


class TestNoteForm(TestCase):
    """
    Testing note form.
    Not required. blank=True in model.
    """
    def test_empty_fields(self):
        """
        Test can be blank.
        """
        form = NoteForm(data={
            'note': '',
        })
        self.assertTrue(form.is_valid())

    def test_integer_in_field(self):
        """
        Can take integer.
        """
        form = NoteForm(data={
            'note': 20,
        })
        self.assertTrue(form.is_valid())

    def test_string_in_field(self):
        """
        Can take string.
        """
        form = NoteForm(data={
            'note': 'Test message'
        })
        self.assertTrue(form.is_valid())

