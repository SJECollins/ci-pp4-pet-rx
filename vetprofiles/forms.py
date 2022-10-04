from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import Vet


class RegistrationForm(UserCreationForm):
    """
    Custom user creation form as we have custom user models.
    """
    email = forms.EmailField(max_length=100,
                             help_text='Required. Add a valid email address')

    class Meta:
        model = Vet
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')


class AccountAuthenticationForm(forms.ModelForm):
    """
    Login form from our Vet object.
    Raises a validation error if email and password don't match
    """
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Vet
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")


class AccountUpdateForm(forms.ModelForm):
    """
    Create an edit form from our Vet object.
    Raises a validation error if tries to edit in existing email.
    """
    class Meta:
        model = Vet
        fields = ('email', 'first_name', 'last_name')

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = Vet.objects.exclude(
                    pk=self.instance.pk).get(
                    email=email)
            except Vet.DoesNotExist:
                return email
            raise forms.ValidationError(
                'Email "%s" is already in use.' %
                account.email)


class ContactForm(forms.Form):
    """
    Simple contact form for visitors to send message to site's email account.
    """
    contact_name = forms.CharField(max_length=200)
    contact_email = forms.EmailField()
    contact_message = forms.CharField(widget=forms.Textarea)
