from django.contrib import admin
from .models import CustomerProfile, LoanRequest
# Register your models here.
# This will help to manage data by admin

admin.site.register(CustomerProfile)
admin.site.register(LoanRequest)