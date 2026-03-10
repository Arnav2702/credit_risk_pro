from django.contrib import admin
from django.urls import path
from django.urls import include # This will help to include the urls of the app in the project
from . import views
# This will help to import the views from the views.py file

admin.site.site_header = "Credit Risk Admin"
admin.site.site_title = "Credit Risk Admin Portal"
admin.site.index_title = "Welcome to Credit Risk Admin Portal"


urlpatterns = [
    path("", views.apply_loan, name="apply_loan"),
    path("loan_list/", views.loan_list, name="loan_list"),
]