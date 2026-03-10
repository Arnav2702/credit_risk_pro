from django.urls import path
from . import views 
from django.urls import include

app_name = 'dashboard_app' # Surname set hai

urlpatterns = [
    path('user/<str:username>/', views.userDashboard, name='user_dashboard'),
    path('user/<str:username>/apply/', views.applyLoan, name='apply_loan'), # <--- username yahan bhi chahiye
    path('user/<str:username>/history/', views.loanHistory, name='loan_history'),
]