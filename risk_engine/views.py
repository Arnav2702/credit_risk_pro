from django.shortcuts import render

# Create your views here.
from .models import CustomerProfile, LoanRequest
from .forms import LoanRequestForm
from .services import calculate_risk_and_interest

from django.utils import timezone

def apply_loan(request):
    if request.method == 'POST':
        form = LoanRequestForm(request.POST)
        if form.is_valid():
            aadhar_number = form.cleaned_data['aadhar_number']
            amount = form.cleaned_data['amount']
            tenure = form.cleaned_data['tenure']

            try:
                #1. Check if customer exists
                customer =CustomerProfile.objects.get(aadhar_number=aadhar_number)

                #2. Calculate risk and interest
                decision = calculate_risk_and_interest(customer, amount)

                #3. Save to Database
                loan_req = LoanRequest.objects.create(
                    customer = customer,
                    loan_amount = amount,
                    tenure = tenure,
                    reason = form.cleaned_data['reason'],
                    status = 'APPROVED' if decision['approved'] else 'REJECTED',
                    interest_rate = decision.get('interest_rate',0),
                    created_at = timezone.now(),
                )

                result = decision
                result['loan_id'] = loan_req.id
            
            except CustomerProfile.DoesNotExist:
                result = {
                    'approved': False,
                    'reason': 'Customer not found',
                    'interest_rate': None,
                    'loan_id': None,
                }

            return render(request, 'risk_engine/apply_loan.html', {'form': form, 'result': result})

def loan_list(request):
    loans = LoanRequest.objects.all()
    return render(request, 'risk_engine/loan_list.html', {'loans': loans})
