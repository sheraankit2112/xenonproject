
from django import forms
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


from django.core import validators

def email_validator(value):
    if User.objects.filter(email=value).exists():
        raise forms.ValidationError("Email already exists")

def username_validator(value):
    if User.objects.filter(username=value).exists():
        raise forms.ValidationError("Username already taken, Choose another one")

class loginform(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password"}))

    def clean(self):
        cleaned_data=super().clean()
        if self.is_valid():
            user=self.cleaned_data['username']
            pas=self.cleaned_data['password']
            authen=authenticate(username=user,password=pas)
            if authen is None:
                raise forms.ValidationError("*Username or password incorrect")

class signupform(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Full name"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Email id"}),validators=[email_validator])
    username=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"username"}),validators=[username_validator])
    contact=forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"contact"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password"}))
    cpassword=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"confirm Password"}))

    def clean(self):
        cleaned_data=super().clean()
        if self.is_valid():
            pas=self.cleaned_data['password']
            cpas=self.cleaned_data['cpassword']
            if pas!=cpas:
                raise forms.ValidationError("Password do not match")


    

        