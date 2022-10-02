import datetime
from django.test import TestCase
from django.urls import reverse
import pytz
from vetprofiles.models import Vet
from records.models import Record
from .models import Drug, Prescription


class TestPrescriptionsNotRegistered(TestCase):
    """
    Testing for views if not logged in.
    Should all redirect to login.
    """
    def setUp(self):
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

    def test_get_drugs_page(self):
        """
        Try to go to records list.
        """
        response = self.client.get('/prescriptions/drugs/', follow=True)
        self.assertRedirects(response, '/login/', status_code=302, target_status_code=200, fetch_redirect_response=True)

    def test_get_drugs_search(self):
        """
        Try to go to records search.
        """
        response = self.client.get('/prescriptions/drug-search/', follow=True)
        self.assertRedirects(response, '/login/', status_code=302, target_status_code=200, fetch_redirect_response=True)

    def test_get_detail_drug(self):
        """
        Try to go to detailed view of drug.
        """
        drug_id = self.drug.id
        response = self.client.get(reverse('prescriptions:detail_drug', args=[drug_id]))
        self.assertRedirects(response, '/login/', status_code=302, target_status_code=200, fetch_redirect_response=True)

    def test_add_prescrip(self):
        """
        Try to go to add prescription.
        """
        animal_id = self.animal.id
        response = self.client.get(reverse('prescriptions:detail_drug', args=[animal_id]))
        self.assertRedirects(response, '/login/', status_code=302, target_status_code=200, fetch_redirect_response=True)

