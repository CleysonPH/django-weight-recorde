from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import SignInForm, SignUpForm, UserProfileForm
from .models import UserProfile


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


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            UserProfile.objects.create(user=user)
            return redirect('accounts:signin')

    form = SignUpForm()
    context = {
        'title': 'Sign Un',
        'form': form,
    }

    return render(request, 'accounts/signup.html', context)


@login_required
def signout(request):
    logout(request)
    return redirect('accounts:signin')


@login_required
def user_profile_update(request):
    user_profile = request.user.userprofile

    if request.method == 'POST':
        form = UserProfileForm(
            request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            form.save()
            return redirect('weight_recorder:dashboard')

    form = UserProfileForm(instance=user_profile)
    context = {
        'title': 'Editar Perfil',
        'form': form,
    }

    return render(request, 'accounts/user_profile_form.html', context)
