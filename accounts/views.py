from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('library:home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print("User",user)
        if user is not None:
            login(request, user)
            return redirect('library:home')  # Redirect to a home page or dashboard
        else:
            return render(request, 'login.html', {'error': '*Invalid username or password'})
        
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')