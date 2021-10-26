from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm #defaul user model of Django
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class OrderForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('image', )

class CreateUserForm(UserCreationForm): #it is actually same form that Django gives but here we are replicating with our customize fields
    class Meta:
        model = User
        fields = ['username','email','password1','password2'] #from the documentation we are taking these values 