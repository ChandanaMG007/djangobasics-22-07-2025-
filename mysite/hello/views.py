from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from datetime import date
from django.contrib.auth import authenticate, login as auth_login

# Homepage
def say_hello(request):
    return render(request, 'hello/home.html')

# Welcome screen
def index(request):
    return render(request, 'hello/index.html')

# Sign up
def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            User.objects.create_user(username=name, password=password)
            return redirect('login')
        else:
            return render(request, 'hello/signup.html', {
                'error': 'Passwords do not match',
                'age_range': range(10, 100)
            })

    return render(request, 'hello/signup.html', {
        'age_range': range(10, 100)
    })

# Login
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('main')  # Go to main dashboard
        else:
            return render(request, 'hello/login.html', {'error': 'Invalid username or password'})
    return render(request, 'hello/login.html')

# Main dashboard
def main(request):
    return render(request, 'hello/main.html')


# ---------------------------
# ✨ Self-Care Feature Views
# ---------------------------

# 🌬️ Breathing Space
def breathing(request):
    return render(request, 'hello/breathing.html')

# ⏱️ Pomodoro Timer
def pomodoro(request):
    return render(request, 'hello/pomodoro.html')

# 📔 Journal
def journal(request):
    return render(request, 'hello/journal.html')
   

# 💧 Water Tracker
def water(request):
    return render(request, 'hello/water.html')

# 📚 Book Space
def quotes(request):
    return render(request, 'hello/quotes.html')

