from django.test import TestCase, RequestFactory
from .models import Vet

# Create your tests here.


class TestVetprofiles(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = Vet.objects.create_user(
            email='test@email.com',
            first_name='test',
            last_name='user',
            password='12345'
            )

    def test_get_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_about(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_get_contact(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_get_register(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vetprofiles/register.html')
    
    def test_get_login(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vetprofiles/login.html')

    def test_get_profile(self):
        self.client.login(email='test@email.com', password='12345')
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vetprofiles/profile.html')
