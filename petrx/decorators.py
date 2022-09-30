from django.shortcuts import render, redirect


def vet_login_and_active(function=None):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_active:
                return function(request, *args, **kwargs)
            else:
                return render(request, 'vetprofiles/restricted.html')
        else:
            return redirect('vetprofiles:login')
    return wrapper
