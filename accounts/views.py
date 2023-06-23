from django.shortcuts import render, redirect
from accounts.form import CustomUserForm
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Details")
            return redirect('login')
    else:
        return render(request,"login.html")


def register(request):
    form = CustomUserForm()
    if request.method =='POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Success You Can Login Now..!")
            return redirect('login')
    return render(request,"register.html",{'form':form})


def logout(request):
    auth.logout(request)
    return redirect('/')