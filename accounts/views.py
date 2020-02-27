from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

from .forms import SignInForm, SignUpForm, UserProfileForm, UserUpdateForm
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
        user_form = UserUpdateForm(request.POST, instance=request.user)
        user_profile_form = UserProfileForm(
            request.POST, request.FILES, instance=user_profile)

        if user_form.is_valid() and user_profile_form.is_valid():
            user_form.save()
            user_profile_form.save()
            messages.success(request, 'Perfil atualizado com sucesso')

            return redirect('weight_recorder:dashboard')

    user_form = UserUpdateForm(instance=request.user)
    user_profile_form = UserProfileForm(instance=user_profile)
    context = {
        'title': 'Atualizar Perfil',
        'user_profile_form': user_profile_form,
        'user_form': user_form,
    }

    return render(request, 'accounts/user_profile_form.html', context)


@login_required
def update_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Senha alterada com sucesso')
            update_session_auth_hash(request, form.user)

            return redirect('weight_recorder:dashboard')

    form = PasswordChangeForm(user=request.user)
    context = {
        'title': 'Alterar Senha',
        'form': form,
    }

    return render(request, 'accounts/update_password.html', context)
