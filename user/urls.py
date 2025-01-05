from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('register', views.registration, name='registration'),
    path('login', views.login, name='login'),
    path('home', views.home, name='home'),
]