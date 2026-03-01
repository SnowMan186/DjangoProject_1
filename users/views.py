from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm, CustomUser
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.views.generic import CreateView

class RegisterView(CreateView):
    model = CustomUser
    form_class = RegistrationForm
    template_name = 'users/register.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        subject = 'Добро пожаловать!'
        message = render_to_string('users/welcome_email.html', {'user': user})
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
        login(self.request, user)
        return super().form_valid(form)

def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Неправильные учетные данные'
    else:
        error_message = ''
    return render(request, 'users/login.html', {'error_message': error_message})