from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.core.mail import send_mail
from django.template.loader import render_to_string
from petrx.decorators import vet_login_and_active
from .forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm, ContactForm


def index(request):
    """
    Render index page.
    """
    return render(request, 'index.html')


def about(request):
    """
    Render about page.
    """
    return render(request, 'about.html')


def contact(request):
    """
    Render contact page.
    Using django's send_mail for testing in development.
    From Code With Stein, see link in README credits.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent.')
            return redirect('vetprofiles:contact')
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)


def register(request):
    """
    Register new user.
    Redirects to index.
    """
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('vetprofiles:index')
        else:
            context = {'registration_form': form}
    else:   # GET request
        form = RegistrationForm()
        context = {'registration_form': form}
    return render(request, 'vetprofiles/register.html', context)


def logout_view(request):
    """
    Logs user out.
    Redirects to index.
    """
    logout(request)
    return redirect('vetprofiles:index')


def login_view(request):
    """
    User login.
    Redirects to user profile.
    """
    if request.user.is_authenticated:
        return redirect('vetprofiles:index')
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('vetprofiles:profile')
    else:
        form = AccountAuthenticationForm()
    context = {'login_form': form}
    return render(request, 'vetprofiles/login.html', context)


@vet_login_and_active
def profile(request):
    """
    Renders user profile.
    Redirects to login page if user not logged in.
    """
    return render(request, 'vetprofiles/profile.html')


@vet_login_and_active
def edit_profile(request):
    """
    Edit user profile.
    Initialises data of current user.
    Redirects to login page if user not logged in.
    """
    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                'email': request.POST['email'],
                'first_name': request.POST['first_name'],
                'last_name': request.POST['last_name'],
            }
            form.save()
            return redirect('vetprofiles:profile')
    else:
        form = AccountUpdateForm(
            initial={
                'email': request.user.email,
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
            }
        )
    context = {'edit_form': form}
    return render(request, 'vetprofiles/edit_profile.html', context)


def user_restricted(request):
    """
    Renders restricted view.
    """
    return render(request, 'vetprofiles/restricted.html')


def handle_not_found(request, exception):
    return render(request, 'not_found.html')
