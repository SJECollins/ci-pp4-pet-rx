import datetime
from django.test import TestCase
import pytz
from .models import Record


class TestRecord(TestCase):
    """
    Testing Record model.
    """

    def test_record(self):
        """
        Testing for creating an animal record
        """
        animal = Record.objects.create(
            name='Bob',
            surname='Bobberson',
            date_of_birth=datetime.datetime(
                2012,
                12,
                12,
                0,
                0,
                0,
                tzinfo=pytz.utc),
            species='Canine',
            breed='JRT',
            weight=12.5,
            note='No notes',
        )
        animal_string = 'Bob Bobberson'
        self.assertEqual(animal.name, 'Bob')
        self.assertEqual(animal.surname, 'Bobberson')
        self.assertEqual(str(animal.date_of_birth),
                         '2012-12-12 00:00:00+00:00')
        self.assertEqual(animal.species, 'Canine')
        self.assertEqual(animal.breed, 'JRT')
        self.assertEqual(animal.weight, 12.5)
        self.assertEqual(animal.note, 'No notes')
        self.assertEqual(animal_string, str(animal))
