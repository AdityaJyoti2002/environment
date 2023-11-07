from django.contrib import admin
from django.urls import path
from icecream import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('home', views.home, name='home'),
    path('event', views.event, name='event'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
]