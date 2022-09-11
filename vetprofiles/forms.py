from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import Vet


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='Required. Add a valid email address')

    class Meta:
        model = Vet
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')


class AccountAuthenticationForm(forms.ModelForm):
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

    class Meta:
        model = Vet
        fields = ('email', 'first_name', 'last_name')

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = Vet.objects.exclude(pk=self.instance.pk).get(email=email)
            except Vet.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use.' % account.email)