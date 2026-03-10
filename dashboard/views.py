# dashboard/views.py
from django.shortcuts import render, redirect
from risk_engine.models import CustomerProfile, LoanRequest
from risk_engine.services import calculate_risk_and_interest
from .forms import LoanRequestForm

def userDashboard(request, username):
    customer = CustomerProfile.objects.get(username=username)
    return render(request, 'dashboard/user_dashboard.html', {'customer': customer})

def applyLoan(request, username):
    customer = CustomerProfile.objects.get(username=username)
    if request.method == 'POST':
        form = LoanRequestForm(request.POST)
        if form.is_valid():
            loan = form.save(commit=False)
            loan.customer = customer
            
            # Risk Engine se decision
            decision = calculate_risk_and_interest(customer, loan.loan_amount)
            
            loan.status = 'APPROVED' if decision['approved'] else 'REJECTED'
            loan.interest_rate = decision['interest_rate']
            loan.save()
            return redirect('dashboard_app:loan_history', username=username)
    else:
        form = LoanRequestForm()
    return render(request, 'dashboard/apply_loan.html', {'form': form, 'customer': customer})

def loanHistory(request, username):
    customer = CustomerProfile.objects.get(username=username)
    # Sirf isi user ka loan history fetch karenge
    loans = LoanRequest.objects.filter(customer=customer).order_by('-created_at')
    return render(request, 'dashboard/history.html', {'loans': loans, 'customer': customer})