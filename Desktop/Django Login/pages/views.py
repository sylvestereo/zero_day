from cProfile import Profile
from ctypes import addressof
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Profile
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='signin')
def index(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'profile.html')

def setting(request):
    return render(request, 'setting.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'signin.html')


def signout(request):
    logout(request)
    return redirect('signin')


def signup(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        address=request.POST['address']
        reason=request.POST['reason']
        state=request.POST['state']
        city=request.POST['city']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exist')
                return redirect('signup')
            else:
                if User.objects.filter(email=email).exists():
                        messages.error(request, 'Email already exists')
                else:
                    form = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password, address=address, state=state, city=city, reason=reason)
                    form.save()

                    user_login = auth.authenticate(username=username, password=password)
                    auth.login(request, user_login)

                    user_model = User.objects.get(username=username)
                    new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                    new_profile.save()
                    return redirect('index')
                # else:
                # messages.success(request, 'Account created successfully')
                # return redirect('signin')
        else:
            messages.error(request, 'Password does not match')
            return redirect('signup')
    return render(request, 'signup.html')
