from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

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

