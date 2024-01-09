from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return render(request, "authentication/index.html")

def signup(request):

    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        myuser = User.objects.create_user(username,email,password1)
        myuser.save()

        messages.success(request, "Your account has been successfully created.")
        
        return redirect('signin')

    return render(request, "authentication/signup.html")

def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']

        user = authenticate(username = username, password = password1)

        if user is not None:
            login(request,user)
            return render(request, "authentication/index.html")
        else:
            messages.error(request, "Incorrect Credentials")
            return redirect('home')
    return render(request, "authentication/signin.html")

def signout(request):

    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('home')