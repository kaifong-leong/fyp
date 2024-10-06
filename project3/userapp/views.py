from django.shortcuts import render, redirect

from . forms import CreateUserForm, LoginForm

from django.contrib.auth.decorators import login_required

# - Authentication models and functions

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

def homepage(request):
    
    return render(request, 'userapp/index.html') # reference template properly

def register(request):
    
    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("my-login") # redirect to the login page after someone registers

    context = {'registerform':form} # add into context dictionary in order to display form

    return render(request, 'userapp/register.html', context=context)

def my_login(request):
    
    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password) # check if username and password matches with database

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")

    context = {'loginform':form}

    return render(request, 'userapp/my-login.html', context=context)

def user_logout(request):

    auth.logout(request)

    return redirect("")

@login_required(login_url="my-login") # protecting our dashboard view to require login first
def dashboard(request):
    
    return render(request, 'userapp/dashboard.html')