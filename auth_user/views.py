from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from auth_user.forms import RegisterForm, LoginForm


# Create your views here.

def register_view(request):
    if request.method == 'GET':
        context_data = {
            'form': RegisterForm
        }
        return render(request, 'users/registration.html', context=context_data)
    if request.method == 'POST':
        data = request.POST
        form = RegisterForm(data)

        if form.is_valid():
            if form.cleaned_data.get('password1') == form.cleaned_data.get('password2'):
                User.objects.create_user(
                    username=form.cleaned_data.get('username'),
                    password=form.cleaned_data.get('password1')
                )
                return redirect('/users/login/')
            else:
                form.add_error('password2', 'password min 8 ')

        context_data = {
            'form': form
        }
        return render(request, 'users/registration.html', context=context_data)


def login_view(request):
    if request.method == 'GET':
        context_data = {
            'form': LoginForm
        }
        return render(request, 'users/login.html', context=context_data)
    if request.method == 'POST':
        data = request.POST
        form = LoginForm(data)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password'),
            )
            if user:
                login(request, user=user)
                return redirect('product_menu')
            else:
                form.add_error('password', 'Incorrect ')
        context_data = {
            'form': form
        }
        return render(request, 'users/login.html', context=context_data)


def logout_view(request):
    logout(request)
    return redirect('product_menu')