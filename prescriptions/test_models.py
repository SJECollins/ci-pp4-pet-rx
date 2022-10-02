import datetime
from django.test import TestCase
from unittest import mock
import pytz
from vetprofiles.models import Vet
from records.models import Record
from .models import Drug, Prescription


class TestDrug(TestCase):
    def test_drug(self):
        """
        Testing for creating a drug.
        """
        drug = Drug.objects.create(
            name='Amoxiclav',
            dose=12.5,
            measure='mg',
            category='Antibiotic',
            route='PO',
            warnings='None'
        )
        drug_string = 'Amoxiclav'
        self.assertEqual(drug.name, 'Amoxiclav')
        self.assertEqual(drug.dose, 12.5)
        self.assertEqual(drug.measure, 'mg')
        self.assertEqual(drug.category, 'Antibiotic')
        self.assertEqual(drug.route, 'PO')
        self.assertEqual(drug.warnings, 'None')
        self.assertEqual(drug_string, str(drug))


class TestPrescription(TestCase):
    def setUp(self):
        self.user_a = Vet.objects.create_user(
            email='test@email.com',
            first_name='test',
            last_name='user',
            password='12345'
            )
        self.user_a.is_active = True
        self.user_a.save()
        self.client.login(email='test@email.com', password='12345')
        self.drug = Drug.objects.create(
            name='Amoxiclav',
            dose=12.5,
            measure='mg',
            category='Antibiotic',
            route='PO',
            warnings='None'
        )
        self.drug.save()
        self.animal = Record.objects.create(
            name='Bob',
            surname='Bobberson',
            date_of_birth=datetime.datetime(2012, 12, 12, 0, 0, 0, tzinfo=pytz.utc),
            species='Canine',
            breed='JRT',
            weight=12.5,
            note='No notes',
        )
        self.animal.save()

    def test_prescription(self):
        mocked = datetime.datetime(2022, 10, 10, 0, 0, 0, tzinfo=pytz.utc)
        with mock.patch('django.utils.timezone.now', mock.Mock(return_value=mocked)):
            prescription = Prescription.objects.create(
                animal=self.animal,
                animal_weight=12.5,
                vet=self.user_a,
                drug=self.drug,
                drug_dose=12.5,
                dose=156.25,
                measure='mg',
                frequency='BID',
                length=5,
                route='PO',
                date=mocked,
            )
        prescription_string = 'Bob 156.25 Amoxiclav test user'
        self.assertEqual(str(prescription.animal), 'Bob Bobberson')
        self.assertEqual(prescription.animal_weight, 12.5)
        self.assertEqual(str(prescription.drug), 'Amoxiclav')
        self.assertEqual(prescription.drug_dose, 12.5)
        self.assertEqual(prescription.dose, 156.25)
        self.assertEqual(prescription.measure, 'mg')
        self.assertEqual(prescription.frequency, 'BID')
        self.assertEqual(prescription.length, 5)
        self.assertEqual(prescription.route, 'PO')
        self.assertEqual(str(prescription.date), '2022-10-10 00:00:00+00:00')
        self.assertEqual(prescription_string, str(prescription))
