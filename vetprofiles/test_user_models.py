from django.contrib.auth import get_user_model
from django.test import TestCase


class UsersManagersTests(TestCase):
    """
    Testing custom user models.
    From Michael Herman on testdriven.io, see link in credits of readme.
    """

    def test_create_user(self):
        """
        Testing for creating a user.

        """
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com', first_name='bob', last_name='bobberson', password='foo')
        user_string = 'bob bobberson'
        self.assertEqual(user.email, 'normal@user.com')
        self.assertEqual(user.first_name, 'bob')
        self.assertEqual(user.last_name, 'bobberson')
        self.assertFalse(user.is_admin)
        self.assertFalse(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertEqual(user_string, str(user))
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', first_name='bob', last_name='bobberson', password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email='super@user.com', first_name='bob', last_name='bobberson', password='foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertEqual(admin_user.first_name, 'bob')
        self.assertEqual(admin_user.last_name, 'bobberson')
        self.assertTrue(admin_user.is_admin)
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
