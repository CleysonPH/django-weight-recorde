from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import SignInForm


def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('weight_recorder:dashboard')

    form = SignInForm()
    context = {
        'title': 'Sign In',
        'form': form,
    }

    return render(request, 'accounts/signin.html', context)
