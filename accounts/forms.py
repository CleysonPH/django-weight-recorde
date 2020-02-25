from django import forms


class SignInForm(forms.Form):
    username = forms.CharField(label='Nome de usuário', required=True)
    password = forms.CharField(
        label='Senha', required=True, widget=forms.PasswordInput)
