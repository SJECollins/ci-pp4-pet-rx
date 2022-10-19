import datetime
from django.test import TestCase
from unittest import mock
import pytz
from vetprofiles.models import Vet
from records.models import Record
from .models import Category, Drug, Prescription


class TestDrug(TestCase):
    """
    Testing drug model.
    """

    def setUp(self):
        self.category = Category.objects.create(
            name='Antibiotic'
        )
        self.category.save()

    def test_drug(self):
        """
        Testing for creating a drug.
        """
        drug = Drug.objects.create(
            name='Amoxiclav',
            dose=12.5,
            measure='mg',
            category=self.category,
            route='PO',
            warnings='None'
        )
        drug_string = 'Amoxiclav'
        self.assertEqual(drug.name, 'Amoxiclav')
        self.assertEqual(drug.dose, 12.5)
        self.assertEqual(drug.measure, 'mg')
        self.assertEqual(str(drug.category), 'Antibiotic')
        self.assertEqual(drug.route, 'PO')
        self.assertEqual(drug.warnings, 'None')
        self.assertEqual(drug_string, str(drug))


class TestPrescription(TestCase):
    """
    Testing prescription model.
    """

    def setUp(self):
        """
        Set up. Create user and animal to work with.
        """
        self.user_a = Vet.objects.create_user(
            email='test@email.com',
            first_name='test',
            last_name='user',
            password='12345'
        )
        self.user_a.is_active = True
        self.user_a.save()
        self.client.login(email='test@email.com', password='12345')
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
        self.drug_b = Drug.objects.create(
            name='Amoxiclav',
            type='Tablet',
            dose=12.5,
            high_dose=15,
            tablet_strength='50, 250, 500',
            measure='mg',
            category=self.category,
            route='PO',
            warnings='None'
        )
        self.drug.save()
        self.animal = Record.objects.create(
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
        self.animal.save()
        self.animal_b = Record.objects.create(
            name='Fluff',
            surname='Flufferson',
            date_of_birth=datetime.datetime(
                2020,
                10,
                10,
                0,
                0,
                0,
                tzinfo=pytz.utc),
            species='Feline',
            breed='DLH',
            weight=3.2,
            note='No notes',
        )
        self.animal_b.save()

    def test_prescription(self):
        """
        Test creating a prescription.
        Need to mock time as have auto_add_now in date field.
        """
        mocked = datetime.datetime(2022, 10, 10, 0, 0, 0, tzinfo=pytz.utc)
        with mock.patch('django.utils.timezone.now', mock.Mock(return_value=mocked)):  # noqa
            prescription = Prescription.objects.create(
                animal=self.animal,
                animal_weight=self.animal.weight,
                vet=self.user_a,
                drug=self.drug,
                drug_dose=self.drug.dose,
                dose='',
                measure='',
                frequency='BID',
                length=5,
                route='',
                date=mocked,
            )
        prescription_string = 'Bob 156.25 Amoxiclav test user'
        self.assertEqual(str(prescription.animal), 'Bob Bobberson')
        self.assertEqual(prescription.animal_weight, 12.5)
        self.assertEqual(str(prescription.drug), 'Amoxiclav')
        self.assertEqual(prescription.drug_dose, 12.5)
        self.assertEqual(prescription.dose, '156.25')
        self.assertEqual(prescription.measure, 'mg')
        self.assertEqual(prescription.frequency, 'BID')
        self.assertEqual(prescription.length, 5)
        self.assertEqual(prescription.route, 'PO')
        self.assertEqual(str(prescription.date), '2022-10-10 00:00:00+00:00')
        self.assertEqual(prescription_string, str(prescription))

    def test_tab_prescription(self):
        """
        Test creating a prescription for tablets.
        Need to mock time as have auto_add_now in date field.
        """
        mocked = datetime.datetime(2022, 10, 10, 0, 0, 0, tzinfo=pytz.utc)
        with mock.patch('django.utils.timezone.now', mock.Mock(return_value=mocked)):  # noqa
            prescription = Prescription.objects.create(
                animal=self.animal,
                animal_weight=self.animal.weight,
                vet=self.user_a,
                drug=self.drug_b,
                type=self.drug_b.type,
                drug_dose=self.drug_b.dose,
                drug_dose_high=self.drug_b.high_dose,
                dose='',
                measure='',
                frequency='BID',
                length=5,
                route='',
                date=mocked,
            )
        prescription_string = 'Bob 0.75tabs x 250 Amoxiclav test user'
        self.assertEqual(str(prescription.animal), 'Bob Bobberson')
        self.assertEqual(prescription.animal_weight, 12.5)
        self.assertEqual(str(prescription.drug), 'Amoxiclav')
        self.assertEqual(prescription.type, 'Tablet')
        self.assertEqual(prescription.drug_dose, 12.5)
        self.assertEqual(prescription.drug_dose_high, 15)
        self.assertEqual(prescription.dose, '0.75tabs x 250')
        self.assertEqual(prescription.measure, 'mg')
        self.assertEqual(prescription.frequency, 'BID')
        self.assertEqual(prescription.length, 5)
        self.assertEqual(prescription.route, 'PO')
        self.assertEqual(str(prescription.date), '2022-10-10 00:00:00+00:00')
        self.assertEqual(prescription_string, str(prescription))

    def test_tab_prescription_out_of_range(self):
        """
        Test creating a prescription for tablets, but not in range.
        Need to mock time as have auto_add_now in date field.
        """
        mocked = datetime.datetime(2022, 10, 10, 0, 0, 0, tzinfo=pytz.utc)
        with mock.patch('django.utils.timezone.now', mock.Mock(return_value=mocked)):  # noqa
            prescription = Prescription.objects.create(
                animal=self.animal_b,
                animal_weight=self.animal_b.weight,
                vet=self.user_a,
                drug=self.drug_b,
                type=self.drug_b.type,
                drug_dose=self.drug_b.dose,
                drug_dose_high=self.drug_b.high_dose,
                dose='',
                measure='',
                frequency='BID',
                length=5,
                route='',
                date=mocked,
            )
        self.assertEqual(prescription.dose, 'No tablets in range.')
        self.assertEqual(prescription.measure, '')
