from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class AccountsManager(BaseUserManager):
    """
    Custom user manager.
    From CodingWithMitch, see link in credits of readme.
    """
    def create_user(self, email, first_name, last_name, password=None):
        """
        Django defaults to username, but in this case want to use email as more
        appropriate.
        Also want to require first and last name as app used in professional
        setting.
        """
        if not email:
            raise ValueError("Email required")
        if not first_name:
            raise ValueError("First name required")
        if not last_name:
            raise ValueError("Last name required")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        """
        Custom superuser.
        """
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Vet(AbstractBaseUser):
    """
    Custom user object.
    From CodingWithMitch, see link in credist of readme.
    """
    email = models.EmailField(verbose_name="email", max_length=80, unique=True)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    # Have to be added for custom user models
    is_admin = models.BooleanField(default=False)
    # is_active initially False, admin to set to True in admin panel
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Set username_field so that we can log in with django
    USERNAME_FIELD = 'email'
    # Mandatory fields
    REQUIRED_FIELDS = ['first_name', 'last_name', ]

    # The objects param references the Accountsmanager to tell the object to use that
    objects = AccountsManager()

    # Return a string of first and last name
    def __str__(self):
        return self.first_name + " " + self.last_name

    # Required permissions
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
