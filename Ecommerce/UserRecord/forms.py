from django import forms
from django.contrib.auth.forms import UserChangeForm,UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import fields
from django.forms import widgets
from django.forms.widgets import Widget
from .models import *

class UserSignUpForm(UserCreationForm):
    username = forms.CharField(label_suffix= '',label='Username ',widget = forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label_suffix= '',label='Your Email ',widget = forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label_suffix= '',label='Your Password ',widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label_suffix= '',label='Confirm Password ',widget = forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields=['username','email']

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label_suffix= '',label='Username ',widget = forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label_suffix= '',label='Password ',widget = forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields=['username','password']


# change user password form 
class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label_suffix= '',label='Enter old password ',widget = forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label_suffix= '',label='Enter new password ',widget = forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label_suffix= '',label='Confirm new password ',widget = forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields=['old_password','new_password1','new_password2']

# user edit profile form 
class userchangeform(UserChangeForm):
    first_name=forms.CharField(label_suffix='',label='First Name ',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name '}))
    last_name=forms.CharField(label_suffix='',label='Last Name',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name '}))
    email=forms.EmailField(label_suffix='',label='Email',widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'user@gmail.com '}))
    password=None
    class Meta:
        model = User
        fields =['first_name','last_name','email']

GENDER = (
    ("Male","Male"),
    ("Female","Female"),
    ("Others","Others"),
)
# user edit profile form 
class profileform(forms.ModelForm):
    mobileno=forms.IntegerField(label_suffix='',label='Contact',widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Mobile NO'}))
    gender =forms.ChoiceField(choices=GENDER,label_suffix=' ',label='Gender')
    class Meta:
        model = Userprofile
        fields = ['mobileno','gender']

        widgets = {
            'gender':forms.TextInput(attrs={'class':'form-control'})
        }