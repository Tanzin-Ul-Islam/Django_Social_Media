from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from login_app.models import *

class createnewuser(UserCreationForm):
    email = forms.EmailField(required = True, label='',
                    widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(required = True, label='',
                    widget=forms.TextInput(attrs={'placeholder': 'User name'}))
    password1 = forms.CharField(required= True ,label='',
                                widget=forms.PasswordInput(attrs={'placeholder':'Set Password'}))
    password2 = forms.CharField(required= True ,label='',
                                widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))
    class Meta:
        model = User
        fields=['email', 'username', 'password1', 'password2']

class Authenticateuser(AuthenticationForm):
    username = forms.CharField(required = True, label='',
                    widget=forms.TextInput(attrs={'placeholder': 'User name'}))
    password = forms.CharField(required= True ,label='',
                                widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    class Meta:
        #model = User
        fields=['username', 'password']

class editprofile(forms.ModelForm):

    dob = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))


    class Meta:
        model = userprofile
        exclude = ['user']

