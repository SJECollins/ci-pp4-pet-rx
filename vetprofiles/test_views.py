from django.test import TestCase
from django.urls import reverse
from .models import Vet
from .forms import RegistrationForm

# Create your tests here.


class TestVetprofilesBase(TestCase):
    """
    Testing views for a user who is not logged in.
    """
    def test_get_index(self):
        """
        Get index page. Test correct template.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_about(self):
        """
        Get about page. Test correct template.
        """
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_get_contact(self):
        """
        Get contact page. Test correct template.
        """
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
    
    def test_submit_contact_form(self):
        response = self.client.post(reverse('vetprofiles:contact'), data={
            'contact_name': 'TestingContact',
            'contact_email': 'testing@contact.com',
            'contact_message': 'This is a test message for the contact form!'
        })
        self.assertRedirects(response, '/contact/', status_code=302, target_status_code=200, fetch_redirect_response=True)

    def test_get_register(self):
        """
        Get register page. Test correct template.
        """
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vetprofiles/register.html')

    def test_register_user(self):
        """
        User registers.
        Test redirects to index page.
        Also test increases user count.
        """
        users = Vet.objects.all()
        self.assertEqual(users.count(), 0)
        response = self.client.post(reverse('vetprofiles:register'), data={
            'email': 'testingregistration@email.com',
            'first_name': 'Notregistered',
            'last_name': 'Buthopefullywillbe',
            'password1': 'AGoodPassw0rd!21dsa',
            'password2': 'AGoodPassw0rd!21dsa'
        })
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, fetch_redirect_response=True)
        self.assertEqual(users.count(), 1)

    def test_get_login(self):
        """
        Get login page. Test correct template.
        """
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vetprofiles/login.html')

    def test_get_profile(self):
        """
        Get profile page.
        Not logged in so should redirect to login.
        """
        response = self.client.get('/profile/', follow=True)
        self.assertRedirects(response, '/login/', status_code=302, target_status_code=200, fetch_redirect_response=True)

    def test_edit_profile(self):
        """
        Get edit profile page.
        Not logged in so should redirect to login.
        """
        response = self.client.get('/edit-profile/', follow=True)
        self.assertRedirects(response, '/login/', status_code=302, target_status_code=200, fetch_redirect_response=True)


class TestUserNotActive(TestCase):
    """
    Testing views for a user who is logged in, but not active.
    Testing the vet_login_and_active decorator
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
        self.client.login(email='test@email.com', password='12345')

    def test_get_login(self):
        """
        Get login page as logged in user, but not active.
        Logged in so should render restricted template.
        """
        response = self.client.get('/login/')
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, fetch_redirect_response=True)

    def test_get_profile(self):
        """
        Get profile page as logged in user, but not active
        Logged in so should render restricted template.
        """
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vetprofiles/restricted.html')

    def test_edit_profile(self):
        """
        Get edit profile page as logged in user, but not active
        Logged in so should render restricted template.
        """
        response = self.client.get('/edit-profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vetprofiles/restricted.html')


class TestUserIsActive(TestCase):
    """
    Testing views for a user who is logged in and is active.
    Testing the vet_login_and_active decorator
    """
    def setUp(self):
        self.user_b = Vet.objects.create_user(
            email='tester@email.com',
            first_name='testing',
            last_name='users',
            password='12345678'
            )
        self.user_b.is_active = True
        self.user_b.save()
        self.client.login(email='tester@email.com', password='12345678')

    def test_get_login(self):
        """
        Get login page. Test correct template.
        """
        response = self.client.get('/login/')
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, fetch_redirect_response=True)

    def test_get_profile(self):
        """
        Get profile page as logged in user and is active
        Logged in so should render profile template.
        """
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vetprofiles/profile.html')

    def test_edit_profile(self):
        """
        Get edit profile page as logged in user and is active
        Logged in so should render edit_profile template.
        """
        response = self.client.get('/edit-profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vetprofiles/edit_profile.html')

    def test_submit_edit_profile(self):
        """
        Test submitted edit form redirects to profile.
        """
        response = self.client.post(reverse('vetprofiles:edit_profile'), data={
            'email': 'tested@email.com',
            'first_name': 'Tester',
            'last_name': 'User',
        })
        self.assertRedirects(response, '/profile/', status_code=302, target_status_code=200, fetch_redirect_response=True)

    def test_logout(self):
        """
        Logout as logged in user.
        Test redirect to index page.
        """
        response = self.client.get('/logout/')
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, fetch_redirect_response=True)


class TestLogin(TestCase):
    """
    Testing login view.
    """
    def setUp(self):
        """
        Set up.
        Create user to work with.
        """
        self.user_c = Vet.objects.create_user(
            email='testinglogin@email.com',
            first_name='testing',
            last_name='users',
            password='ThisIsAREalPW1232!!'
            )
        self.user_c.is_active = True
        self.user_c.save()

    def test_login_user(self):
        """
        Logging in should redirect to profile.
        """
        response = self.client.post(reverse('vetprofiles:login'), data={
            'email': 'testinglogin@email.com',
            'password': 'ThisIsAREalPW1232!!'
        }, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertRedirects(response, '/profile/', status_code=302, target_status_code=200, fetch_redirect_response=True)
 

class TestErrorHandlers(TestCase):
    """
    Testing error handler views.
    """
    def test_custom_404(self):
        """
        Going to a page that doesn't exist should render the custom 404 template.
        """
        response = self.client.get('/thisisnonsense/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'errors/404.html')
