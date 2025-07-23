from django.shortcuts import render

def say_hello(request):
    return render(request, 'hello/home.html')

def index(request):
    return render(request, 'hello/index.html') 