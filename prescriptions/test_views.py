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
        self.user_a = Vet.objects.create_user(
            email='test@email.com',
            first_name='test',
            last_name='user',
            password='12345'
            )
        self.user_a.is_active = False
        self.user_a.save()
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
        self.prescription = Prescription.objects.create(
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
            date=datetime.datetime(2022, 10, 10, 0, 0, 0, tzinfo=pytz.utc),
        )
        self.prescription.save()

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
        response = self.client.get(reverse('prescriptions:add_prescrip', args=[animal_id]))
        self.assertRedirects(response, '/login/', status_code=302, target_status_code=200, fetch_redirect_response=True)

    def test_edit_prescrip(self):
        """
        Try to go to edit prescription.
        """
        prescrip_id = self.prescription.id
        response = self.client.get(reverse('prescriptions:edit_prescrip', args=[prescrip_id]))
        self.assertRedirects(response, '/login/', status_code=302, target_status_code=200, fetch_redirect_response=True)

    def test_list_prescrip(self):
        """
        Try to go to list prescription on animal record.
        """
        prescrip_id = self.prescription.id
        response = self.client.get(reverse('prescriptions:list_prescrip', args=[prescrip_id]))
        self.assertRedirects(response, '/login/', status_code=302, target_status_code=200, fetch_redirect_response=True)

    def test_list_prescrip_vet(self):
        """
        Try to go to list prescription on vet profile.
        """
        response = self.client.get(reverse('prescriptions:vet_prescrip'))
        self.assertRedirects(response, '/login/', status_code=302, target_status_code=200, fetch_redirect_response=True)

    def test_detail_prescrip(self):
        """
        Try to go to list prescription on animal record.
        """
        prescrip_id = self.prescription.id
        response = self.client.get(reverse('prescriptions:detail_prescrip', args=[prescrip_id]))
        self.assertRedirects(response, '/login/', status_code=302, target_status_code=200, fetch_redirect_response=True)

    def test_delete_prescrip(self):
        """
        Try to go to list prescription on animal record.
        """
        prescrip_id = self.prescription.id
        response = self.client.get(reverse('prescriptions:delete_prescrip', args=[prescrip_id]))
        self.assertRedirects(response, '/login/', status_code=302, target_status_code=200, fetch_redirect_response=True)


class TestPrescriptionsNotIsActive(TestCase):
    """
    Testing for views if logged in, but not is_active.
    Should all render restricted.html.
    """
    def setUp(self):
        self.factory = RequestFactory()
        self.user_a = Vet.objects.create_user(
            email='test@email.com',
            first_name='test',
            last_name='user',
            password='12345'
            )
        self.user_a.is_active = False
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
        self.prescription = Prescription.objects.create(
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
            date=datetime.datetime(2022, 10, 10, 0, 0, 0, tzinfo=pytz.utc),
        )
        self.prescription.save()

    def test_get_drugs_page(self):
        """
        Try to go to drugs list.
        """
        response = self.client.get('/prescriptions/drugs/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vetprofiles/restricted.html')

    def test_get_drugs_search(self):
        """
        Try to go to drug search.
        """
        response = self.client.get('/prescriptions/drug-search/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vetprofiles/restricted.html')

    def test_get_detail_drug(self):
        """
        Try to go to detailed view of drug.
        """
        drug_id = self.drug.id
        response = self.client.get(reverse('prescriptions:detail_drug', args=[drug_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vetprofiles/restricted.html')

    def test_add_prescrip(self):
        """
        Try to go to add prescription.
        """
        animal_id = self.animal.id
        response = self.client.get(reverse('prescriptions:add_prescrip', args=[animal_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vetprofiles/restricted.html')

    def test_edit_prescrip(self):
        """
        Try to go to edit prescription.
        """
        prescrip_id = self.prescription.id
        response = self.client.get(reverse('prescriptions:edit_prescrip', args=[prescrip_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vetprofiles/restricted.html')

    def test_list_prescrip(self):
        """
        Try to go to list prescription on animal record.
        """
        prescrip_id = self.prescription.id
        response = self.client.get(reverse('prescriptions:list_prescrip', args=[prescrip_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vetprofiles/restricted.html')

    def test_list_prescrip_vet(self):
        """
        Try to go to list prescription on vet profile.
        """
        response = self.client.get(reverse('prescriptions:vet_prescrip'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vetprofiles/restricted.html')

    def test_detail_prescrip(self):
        """
        Try to go to list prescription on animal record.
        """
        prescrip_id = self.prescription.id
        response = self.client.get(reverse('prescriptions:detail_prescrip', args=[prescrip_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vetprofiles/restricted.html')

    def test_delete_prescrip(self):
        """
        Try to go to list prescription on animal record.
        """
        prescrip_id = self.prescription.id
        response = self.client.get(reverse('prescriptions:delete_prescrip', args=[prescrip_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vetprofiles/restricted.html')


class TestPrescriptionsIsActive(TestCase):
    """
    Testing for views if logged in and is_active.
    """
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
        self.prescription = Prescription.objects.create(
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
            date=datetime.datetime(2022, 10, 10, 0, 0, 0, tzinfo=pytz.utc),
        )
        self.prescription.save()

    def test_get_drugs_page(self):
        """
        Try to go to records list.
        """
        response = self.client.get('/prescriptions/drugs/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'prescriptions/drugs.html')

    def test_get_drugs_search(self):
        """
        Try to go to records search.
        """
        response = self.client.get('/prescriptions/drug-search/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'prescriptions/drug_search.html')

    def test_get_detail_drug(self):
        """
        Try to go to detailed view of drug.
        """
        drug_id = self.drug.id
        response = self.client.get(reverse('prescriptions:detail_drug', args=[drug_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'prescriptions/detail_drug.html')

    def test_add_prescrip(self):
        """
        Try to go to add prescription.
        """
        animal_id = self.animal.id
        response = self.client.get(reverse('prescriptions:add_prescrip', args=[animal_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'prescriptions/add_prescrip.html')

    def test_edit_prescrip(self):
        """
        Try to go to edit prescription.
        """
        prescrip_id = self.prescription.id
        response = self.client.get(reverse('prescriptions:edit_prescrip', args=[prescrip_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'prescriptions/edit_prescrip.html')

    def test_list_prescrip(self):
        """
        Try to go to list prescription on animal record.
        """
        prescrip_id = self.prescription.id
        response = self.client.get(reverse('prescriptions:list_prescrip', args=[prescrip_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'prescriptions/list_prescrip.html')

    def test_list_prescrip_vet(self):
        """
        Try to go to list prescription on vet profile.
        """
        response = self.client.get(reverse('prescriptions:vet_prescrip'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'prescriptions/list_prescrip_vet.html')

    def test_detail_prescrip(self):
        """
        Try to go to list prescription on animal record.
        """
        prescrip_id = self.prescription.id
        response = self.client.get(reverse('prescriptions:detail_prescrip', args=[prescrip_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'prescriptions/detail_prescrip.html')

    def test_delete_prescrip(self):
        """
        Try to go to list prescription on animal record.
        """
        prescrip_id = self.prescription.id
        response = self.client.get(reverse('prescriptions:delete_prescrip', args=[prescrip_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'prescriptions/delete_confirm.html')
