from enum import unique
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from localflavor.in_.models import INPANCardNumberField

class CustomerProfile(models.Model):
    username = models.CharField(max_length=50, primary_key=True) 
    
    password_validator = RegexValidator(
        regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
        message="Password must be at least 8 characters long, include uppercase, lowercase, number and special character."
    )
    password = models.CharField(max_length=100, validators=[password_validator])

    pan_number = INPANCardNumberField(unique=True, blank=False, null=False)
    aadhar_number = models.CharField(max_length=12, blank=True, null=True)
    full_name = models.CharField(max_length=100, default="Unknown")
    monthly_income = models.DecimalField(max_digits=10, decimal_places=2)
    current_total_debt = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    cibil_score = models.IntegerField(default=600)
    is_salaried = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.full_name} ({self.aadhar_number})"

class LoanRequest(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]
    
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    loan_amount = models.DecimalField(max_digits=15, decimal_places=2)
    tenure = models.IntegerField()
    reason = models.TextField()
    

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    interest_rate = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Loan {self.id} - {self.customer.full_name}"