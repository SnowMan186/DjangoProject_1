from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            subject = 'Добро пожаловать!'
            message = render_to_string('users/welcome_email.html', {'user': user})
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Неправильный Email или пароль'
    else:
        error_message = ''
    return render(request, 'users/login.html', {'error_message': error_message})