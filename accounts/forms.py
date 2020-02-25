from django import forms
from django.contrib.auth.models import User


class SignInForm(forms.Form):
    username = forms.CharField(label='Nome de usuário', required=True)
    password = forms.CharField(
        label='Senha', required=True, widget=forms.PasswordInput)


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
