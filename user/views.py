from django.shortcuts import render, redirect, HttpResponse
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def registration(request):

    if request.method == 'POST':
        print('Registering Form')
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) # creates user data
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            print('Registered successfully')
            return redirect(reverse('user:login'))
        else:
            print('Form is invalid:', form.errors)
    else:
        form = RegisterForm()

    return render(request, 'registration.html', {'form':form})
    # return HttpResponse('Registration')

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if not User.objects.filter(username = username).exists():
                print('Username does not exists')
            else:
                user = authenticate(username=username, password=password)
                if user is not None:
                    auth_login(request, user)
                    return redirect(reverse('user:home'))
                else:
                    print('incorrect passowrd')
        else:
            print(form.errors)

    return render(request, 'login.html')

@login_required
def home(request):
    return render(request, 'home.html')