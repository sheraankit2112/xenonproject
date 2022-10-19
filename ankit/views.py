from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from ankit.forms import loginform,signupform
from tables.models import contactformdata,userbio


def homepage(request):
    if request.method=="POST":
        name=request.POST.get("name")
        mobile=request.POST.get("mobile")
        email=request.POST.get("email")
        message=request.POST.get("message")

        contactformdata(name=name,contact=mobile,email=email,message=message).save()
        messages.success(request,"submitted successfully,please refresh")
        return redirect("/")
        
    return render(request,"homepage.html")

def signuppage(request):
    fm=signupform()
    if request.method=="POST":
        fm=signupform(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data["name"]
            username=fm.cleaned_data["username"]
            email=fm.cleaned_data["email"]
            contact=fm.cleaned_data["contact"]
            password=fm.cleaned_data["password"]
            new_user=User.objects.create_user(username,email,password)
            userbio(name=name,mobile=contact,email=email).save()
            messages.success(request,"Account created successfully,refresh page")
            return redirect("/")
    return render(request,"signup.html",{"form":fm})

def loginpage(request):
    fm=loginform()
    if request.method=="POST":
        fm=loginform(request.POST)
        if fm.is_valid():
            global username
            username=fm.cleaned_data["username"]
            password=fm.cleaned_data["password"]
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("/afterlogin")

    return render(request,"login.html",{"form":fm})

def afterlogin(request):
    
    return render(request,"afterlogin.html")

def logoutp(request):
    logout(request)
    return redirect("/")
