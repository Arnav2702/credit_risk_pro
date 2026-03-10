from django import forms
from risk_engine.models import LoanRequest

class LoanRequestForm(forms.ModelForm):
    class Meta:
        model = LoanRequest
        fields = ['loan_amount', 'tenure', 'reason']
        widgets = {
            'loan_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '₹ Loan Amount'}),
            'tenure': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Months (e.g. 12)'}),
            'reason': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Enter loan reason'}),
        }