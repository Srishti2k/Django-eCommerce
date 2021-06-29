from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import fields, widgets
from django.utils.translation import gettext , gettext_lazy as _
#usercreation is inherted in registration
#authentication form is inherted in login 
class CustomerRegistrationForm(UserCreationForm):
    password1= forms.CharField(label='Password' , widget=forms.PasswordInput(attrs={'class' : 'form-control'}))

    password2= forms.CharField(label='Confirm Password (again)' , widget=forms.PasswordInput(attrs={'class' : 'form-control'}))

    email= forms.CharField(required= True , label='Email' , widget=forms.EmailInput(attrs={'class' : 'form-control'}))

    class Meta:
        model= User
        fields = ['username' , 'email' , 'password1' , 'password2' ]
        widgets = {'username' : forms.TextInput(attrs={'class' : 'form-control'})}

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class' : 'form-control' , 'autofocus' : True}))
    password= forms.CharField(label=_("Password") , strip= False , widget=forms.PasswordInput(attrs={'class' : 'form-control' , 'autocomplete' : 'current-password'}))
