from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


from .models import User
from .forms import UserSignupForm, UserLoginForm





def login(request):
    if request.method == 'GET':
        form = UserLoginForm()
        context = {'form': form}
        return render(request, 'accounts/login.html', context)

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            # print("email", email)
            user = authenticate(
                request, 
                email=email, 
                password=password
            )
            # print('user', user)
            if user is not None:
                login(request)
                print("after login")
                messages.success(request, 'User logged in')
                return redirect('/home/')
                
        context = {'form': form}
        return render(request, 'accounts/login.html', context)

def signup(request):
    if request.method == 'GET':
        form = UserSignupForm()
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)

    if request.method == 'POST':
        form = UserSignupForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created!!')
            form = UserSignupForm()
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    

    

