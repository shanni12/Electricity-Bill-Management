from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Complaint


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# class ComplaintForm(forms.Form):
#     bill_id = forms.CharField(max_length=100)
#     issue = forms.CharField(max_length=300)

#     class Meta:
#         model = Complaint
#         fields = ['bill_id', 'issue']
