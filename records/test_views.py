import datetime
from django.test import TestCase
from django.urls import reverse
import pytz
from vetprofiles.models import Vet
from .models import Record


class TestRecordsNotRegistered(TestCase):
    """
    Testing for views if not logged in.
    Should all redirect to login.
    """

    def setUp(self):
        """
        Set up.
        Create animal object to work with.
        """
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

    def test_get_records_page(self):
        """
        Try to go to records list.
        """
        response = self.client.get('/records/', follow=True)
        self.assertRedirects(
            response,
            '/login/',
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True)

    def test_get_records_search(self):
        """
        Try to go to records search.
        """
        response = self.client.get('/records/record-search/', follow=True)
        self.assertRedirects(
            response,
            '/login/',
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True)

    def test_get_add_animal(self):
        """
        Try to go to add animal.
        """
        response = self.client.get('/records/add-animal/', follow=True)
        self.assertRedirects(
            response,
            '/login/',
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True)

    def test_get_animal_profile(self):
        """
        Try to go to animal record.
        """
        animal_id = self.animal.id
        response = self.client.get(
            reverse('records:animal_profile', args=[animal_id]))
        self.assertRedirects(
            response,
            '/login/',
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True)

    def test_get_edit_animal(self):
        """
        Try to go to edit animal.
        """
        animal_id = self.animal.id
        response = self.client.get(
            reverse('records:edit_animal', args=[animal_id]))
        self.assertRedirects(
            response,
            '/login/',
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True)

    def test_get_update_weight(self):
        """
        Try to go to update weight.
        """
        animal_id = self.animal.id
        response = self.client.get(
            reverse('records:update_weight', args=[animal_id]))
        self.assertRedirects(
            response,
            '/login/',
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True)

    def test_get_edit_notes(self):
        """
        Try to go to edit notes.
        """
        animal_id = self.animal.id
        response = self.client.get(
            reverse('records:edit_notes', args=[animal_id]))
        self.assertRedirects(
            response,
            '/login/',
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True)


class TestRecordsNotIsActive(TestCase):
    """
    Testing for views if logged in, but not is_active.
    Should all render restricted.html.
    """

    def setUp(self):
        """
        Set up.
        Create user and animal to work with.
        """
        self.user_b = Vet.objects.create_user(
            email='test@email.com',
            first_name='test',
            last_name='user',
            password='12345'
        )
        self.user_b.is_active = False
        self.user_b.save()
        self.client.login(email='test@email.com', password='12345')

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

    def test_get_records_page(self):
        """
        Try to go to records list.
        """
        response = self.client.get('/records/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vetprofiles/restricted.html')

    def test_get_records_search(self):
        """
        Try to go to records search.
        """
        response = self.client.get('/records/record-search/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vetprofiles/restricted.html')

    def test_get_add_animal(self):
        """
        Try to go to add animal.
        """
        response = self.client.get('/records/add-animal/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vetprofiles/restricted.html')

    def test_get_animal_profile(self):
        """
        Try to go to animal record.
        """
        animal_id = self.animal.id
        response = self.client.get(
            reverse('records:animal_profile', args=[animal_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vetprofiles/restricted.html')

    def test_get_edit_animal(self):
        """
        Try to go to edit animal.
        """
        animal_id = self.animal.id
        response = self.client.get(
            reverse('records:edit_animal', args=[animal_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vetprofiles/restricted.html')

    def test_get_update_weight(self):
        """
        Try to go to update weight.
        """
        animal_id = self.animal.id
        response = self.client.get(
            reverse('records:update_weight', args=[animal_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vetprofiles/restricted.html')

    def test_get_edit_notes(self):
        """
        Try to go to edit notes.
        """
        animal_id = self.animal.id
        response = self.client.get(
            reverse('records:edit_notes', args=[animal_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vetprofiles/restricted.html')


class TestRecordViews(TestCase):
    """
    Testing views for user who is logged in and is active.
    """

    def setUp(self):
        """
        Set up.
        Create user and animal to work with.
        """
        self.user_a = Vet.objects.create_user(
            email='tester@email.com',
            first_name='testing',
            last_name='users',
            password='12345678'
        )
        self.user_a.is_active = True
        self.user_a.save()
        self.client.login(email='tester@email.com', password='12345678')

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

    def test_get_records_page(self):
        """
        Try to go to records list.
        """
        response = self.client.get('/records/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'records/records.html')

    def test_get_records_search(self):
        """
        Try to go to records search.
        """
        response = self.client.get('/records/record-search/', q=['bob'],
                                   follow=True)
        self.assertQuerysetEqual(
            Record.objects.filter(surname__icontains='bob'),
            ['<Record: Bob Bobberson>'])
        self.assertQuerysetEqual(
            Record.objects.filter(name__icontains='bob'),
            ['<Record: Bob Bobberson>'])
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'records/record_search.html')

    def test_get_add_animal(self):
        """
        Try to go to add animal.
        """
        response = self.client.get('/records/add-animal/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'records/add_animal.html')

    def test_add_animal(self):
        """
        Test adding animal redirects to record list.
        """
        response = self.client.post(reverse('records:add_animal'), data={
            'name': 'Fluff',
            'surname': 'Flufferson',
            'date_of_birth': '02/02/2020',
            'species': 'Feline',
            'breed': 'DLH',
            'sex': 'FN',
            'weight': 3
        })
        self.assertRedirects(
            response,
            '/records/',
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True)

    def test_get_animal_profile(self):
        """
        Try to go to animal record.
        """
        animal_id = self.animal.id
        response = self.client.get(
            reverse('records:animal_profile', args=[animal_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'records/animal_profile.html')

    def test_get_edit_animal(self):
        """
        Try to go to edit animal.
        """
        animal_id = self.animal.id
        response = self.client.get(
            reverse('records:edit_animal', args=[animal_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'records/edit_animal.html')

    def test_edit_animal(self):
        """
        Test post redirects to animal's record.
        """
        animal_id = self.animal.id
        response = self.client.post(
            reverse('records:edit_animal', args=[animal_id]),
            data={
                'name': 'Bob',
                'surname': 'Bobberson',
                'date_of_birth': '12/12/2012',
                'species': 'Canine',
                'breed': 'JRT',
                'sex': 'MN',
                'weight': 12})
        self.assertRedirects(
            response,
            '/records/animal-profile/1',
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True)

    def test_get_update_weight(self):
        """
        Try to go to update weight.
        """
        animal_id = self.animal.id
        response = self.client.get(
            reverse('records:update_weight', args=[animal_id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'records/update_weight.html')

    def test_update_weight(self):
        """
        Try to update animal's weight.
        """
        animal_id = self.animal.id
        response = self.client.post(
            reverse('records:update_weight', args=[animal_id]), data={
                'weight': 11
            })
        self.assertEqual(response.status_code, 204)

    def test_get_edit_notes(self):
        """
        Try to go to edit notes.
        """
        animal_id = self.animal.id
        response = self.client.get(
            reverse('records:edit_notes', args=[animal_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'records/edit_notes.html')

    def test_edit_notes(self):
        """
        Try to edit notes.
        """
        animal_id = self.animal.id
        response = self.client.post(
            reverse('records:edit_notes', args=[animal_id]), data={
                'note': 'This is a new note'
            })
        self.assertEqual(response.status_code, 204)
