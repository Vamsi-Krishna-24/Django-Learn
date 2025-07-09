from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.

#Home view
def home(request):
    return render(request, 'home/home.html')

#Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request,'home/login.html',{'error': 'Invalid username or password'})
    return render(request, 'home/login.html')


def get_started(request):
    return render(request, 'home/get_started.html')

def tailwind(request):
    return render(request, 'home/tailwind.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email    = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Password match check
        if password1 != password2:
            messages.error(request, 'Passwords do not match!')
            return render(request, 'home/register.html')

        # Check if user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken!')
            return render(request, 'home/register.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered!')
            return render(request, 'home/register.html')

        # Create user
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        messages.success(request, 'Account created! You can now log in.')
        return redirect('login')  # name of your login route

    return render(request, 'home/register.html')

def logout_view(request):
    logout(request)  # clears the session and logs out the user
    return redirect('home') 



