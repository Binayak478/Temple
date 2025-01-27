from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as LOGIN
# from ..forms import LoginForm


def login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            LOGIN(request,user)
            return redirect("add_event")
        else:
            return redirect("login")
    return render(request,"auth/login.html")