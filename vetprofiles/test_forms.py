from django.test import TestCase
from .models import Vet
from .forms import ContactForm, RegistrationForm, AccountAuthenticationForm, AccountUpdateForm


class TestContactForm(TestCase):
    """
    Testing contact form for required fields.
    """
    def test_empty_fields(self):
        """
        Empty fields should return error.
        """
        form = ContactForm(data={
            'contact_name': '',
            'contact_email': '',
            'contact_message': '',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['contact_name'][0], 'This field is required.')
        self.assertEqual(form.errors['contact_email'][0], 'This field is required.')
        self.assertEqual(form.errors['contact_message'][0], 'This field is required.')

    def test_valid_form(self):
        """
        Form is valid if all fields filled.
        """
        form = ContactForm(data={
            'contact_name': 'Test User',
            'contact_email': 'test@email.com',
            'contact_message': 'This is a test message',
        })
        self.assertTrue(form.is_valid())


class TestRegistrationForm(TestCase):
    """
    Testing registration form for required fields.
    """
    def test_empty_fields(self):
        """
        Empty fields should return error.
        """
        form = RegistrationForm(data={
            'email': '',
            'first_name': '',
            'last_name': '',
            'password1': '',
            'password2': '',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'][0], 'This field is required.')
        self.assertEqual(form.errors['first_name'][0], 'This field is required.')
        self.assertEqual(form.errors['last_name'][0], 'This field is required.')
        self.assertEqual(form.errors['password1'][0], 'This field is required.')
        self.assertEqual(form.errors['password2'][0], 'This field is required.')

    def test_valid_form(self):
        """
        Form is valid if all fields filled.
        """
        form = RegistrationForm(data={
            'email': 'testing@email.com',
            'first_name': 'Tester',
            'last_name': 'User',
            'password1': 'secretPass1!',
            'password2': 'secretPass1!',
        })
        self.assertTrue(form.is_valid())


class TestAccountAuthenticationForm(TestCase):
    """
    Testing login form for required fields.
    """
    def setUp(self):
        self.user_a = Vet.objects.create_user(
            email='tester@email.com',
            first_name='testing',
            last_name='users',
            password='12345678'
            )
        self.user_a.is_active = True
        self.user_a.save()
        self.client.login(email='tester@email.com', password='12345678')

    def test_empty_fields(self):
        """
        Empty fields should return error.
        """
        form = AccountAuthenticationForm(data={
            'email': '',
            'password': '',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'][0], 'This field is required.')
        self.assertEqual(form.errors['password'][0], 'This field is required.')

    def test_invalid_password(self):
        """
        Password doesn't match registered email.
        """
        form = AccountAuthenticationForm(data={
            'email': 'tester@email.com',
            'password': '12345',
        })
        self.assertFalse(form.is_valid())

    def test_valid_form(self):
        """
        Form is valid if all fields filled.
        """
        form = AccountAuthenticationForm(data={
            'email': 'tester@email.com',
            'password': '12345678',
        })
        self.assertTrue(form.is_valid())


class TestAccountUpdateForm(TestCase):
    """
    Testing edit form for required fields.
    """
    def setUp(self):
        self.user_a = Vet.objects.create_user(
            email='tester@email.com',
            first_name='testing',
            last_name='users',
            password='12345678'
            )
        self.user_a.is_active = True
        self.user_a.save()
        self.client.login(email='tester@email.com', password='12345678')
        self.user_b = Vet.objects.create_user(
            email='testing@email.com',
            first_name='tested',
            last_name='useragain',
            password='12345678910'
            )
        self.user_b.is_active = True
        self.user_b.save()

    def test_empty_fields(self):
        """
        Empty fields should return error.
        """
        form = AccountUpdateForm(data={
            'email': '',
            'first_name': '',
            'last_name': '',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'][0], 'This field is required.')
        self.assertEqual(form.errors['first_name'][0], 'This field is required.')
        self.assertEqual(form.errors['last_name'][0], 'This field is required.')

    def test_form_email_error(self):
        """
        Form raises validation error if tries to use existing email.
        """
        form = AccountUpdateForm(data={
                'email': 'tester@email.com',
                'first_name': 'Test',
                'last_name': 'User',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['Email "tester@email.com" is already in use.'])

    def test_valid_form(self):
        """
        Form is valid if all fields filled.
        """
        form = AccountUpdateForm(data={
            'email': 'test@email.com',
            'first_name': 'Test',
            'last_name': 'User',
        })
        self.assertTrue(form.is_valid())
