from django.urls import path
from hello import views
from .views import journal


urlpatterns = [
    path('', views.say_hello, name='say_hello'),         
    path('hello/index/', views.index, name='index'),      
    path('hello/login/', views.login, name='login'),       
    path('hello/signup/', views.signup, name='signup'),    
    path('hello/main/', views.main, name='main'),          

    path('hello/breathing/', views.breathing, name='breathing'),

    path('hello/pomodoro/', views.pomodoro, name='pomodoro'),

    path('hello/journal/', views.journal, name='journal'),

    path('hello/water/', views.water, name='water'),

    path('hello/quotes/', views.quotes, name='quotes'),


]



