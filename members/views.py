from members.models import Registration
from django.contrib.auth.backends import RemoteUserBackend
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User, auth
from . models import Registration

# Create your views here.
def register(request):
    if request.method == 'POST':
        full_name = request.POST['full-name']
        email = request.POST['email']
        skills = request.POST['skills']
        desc = request.POST['desc']
        experience = request.POST['experience']
        calendly = request.POST['calendly']

        register = Registration(name=full_name,email=email,skills=skills,description=desc,experience=experience,calendly=calendly)
        register.save()

        return redirect('home')
    else:
        return render(request,'register.html',{})

def signup_user(request):
    if request.method == "POST":
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.success(request,("User with this username already exists!!"))
                return redirect('login')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                messages.success(request,("Registered Successfully...Log In Now..."))
                return redirect('login')
        else:
            messages.success(request,("Password is not matching!!"))
            return redirect('signup.html')
    else:
        return render(request,'signup.html',{})

def logout_user(request):
    logout(request)
    return redirect('home')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    else:
        return render(request,'login.html',{})