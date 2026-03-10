from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views # This will help to include the urls of the app in the project

app_name = 'home_app' # Surname set

urlpatterns = [
    path("", views.index, name="index"),
    path("index/", views.index),
    path("login/", views.login, name="login"), # This will help to login the user   
    path("register/", views.register, name="register"), # This will help to register the user
    path("create_password/", views.create_password, name="create_password"), # This will help to create the password
    path("add_details/", views.add_details, name="add_details"), # This will help to add the details

]
