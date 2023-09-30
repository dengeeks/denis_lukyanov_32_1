from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=32, min_length=3)
    password1 = forms.CharField(max_length=64, min_length=8, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=64, min_length=8, widget=forms.PasswordInput())


class LoginForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=32)
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())
