from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import include
from django.contrib import messages
from risk_engine.models import CustomerProfile
from django.contrib.auth import authenticate
from django.contrib.sessions.models import Session
import re

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = CustomerProfile.objects.get(username=username, password=password)
            
            request.session['logged_in_user'] = user.username
            messages.success(request, f'Welcome {username}') 
            return redirect('dashboard_app:user_dashboard', username=user.username)
            
        except CustomerProfile.DoesNotExist:
            messages.error(request, 'Invalid username or password')
            return redirect('home_app:login')
    return render(request, 'home/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        #check if the username is already in the database
        if CustomerProfile.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('home_app:register')
        else:
            # saving the username and redirect to create password page
            request.session['username'] = username # This will help to save the username in the session
            return redirect('home_app:create_password')
    return render(request, 'home/register.html')

def create_password(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        #Password must be at least 8 characters long, include uppercase, lowercase, number and special character.
        if len(password) < 8:
            messages.error(request, 'Password must be at least 8 characters long')
            return redirect('home_app:create_password')
        if not re.search(r'[A-Z]', password):
            messages.error(request, 'Password must include uppercase letter')
            return redirect('home_app:create_password')
        if not re.search(r'[a-z]', password):
            messages.error(request, 'Password must include lowercase letter')
            return redirect('home_app:create_password')
        if not re.search(r'\d', password):
            messages.error(request, 'Password must include number')
            return redirect('home_app:create_password')
        
        if password == confirm_password:
            # save the password and redirect to add_details page
            request.session['password'] = password # This will help to save the password in the session
            return redirect('home_app:add_details')
        else:
            messages.error(request, 'Password and Confirm Password do not match')
            return redirect('home_app:create_password')
    return render(request, 'home/create_password.html')

def add_details(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        pan_number = request.POST['pan_number']
        aadhar_number = request.POST['aadhar_number']
        monthly_income = request.POST['monthly_income']
        current_total_debt = request.POST['current_total_debt']
        cibil_score = request.POST['cibil_score']
        is_salaried='is_salaried' in request.POST

        #saving username, password and all details in the database
        customer = CustomerProfile.objects.create(username=request.session['username'],
         password=request.session['password'], 
         full_name=full_name, 
         pan_number=pan_number, 
         aadhar_number=aadhar_number,
         monthly_income=monthly_income, 
         current_total_debt=current_total_debt,
         cibil_score=cibil_score,
         is_salaried=is_salaried)
        customer.save()
        messages.success(request, 'Details added successfully')

        request.session['logged_in_user'] = customer.username
        
        return redirect('dashboard_app:user_dashboard', username=customer.username) # dashboard is for that specific user only and this url is in the risk_engine app
    return render(request, 'home/add_details.html')

