from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('index')
        else:
            context = {
                'registration_form': form
            }
    else:   # GET request
        form = RegistrationForm()
        context = {
            'registration_form': form
        }
    return render(request, 'accounts/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('index')


def login_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect('index')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('index')

    else:
        form = AccountAuthenticationForm()

    context = {
        'login_form': form
    }
    return render(request, 'accounts/login.html', context)


def edit_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                'email': request.POST['email'],
                'first_name': request.POST['first_name'],
                'last_name': request.POST['last_name'],
            }
            form.save()
            context = {
                'success_message': 'Updated'
            }
    else:
        form = AccountUpdateForm(
            initial={
                'email': request.user.email,
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
            }
        )
    context = {
        'edit_form': form
    }
    return render(request, 'accounts/edit_account.html', context)
