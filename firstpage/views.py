from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
	

def home(request):
	return render(request,'registration.html')

def signup(request):
    if request.method=="POST":
        username = request.POST['username']
        emailid = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username,email=emailid,password=password)
        user.save()
        return redirect('/')
    else:
        return render(request,'signup.html')

def login(request):
    if request.method == "POST":
        emailid = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=emailid, password=password)
        if user is not None:
            print ('hello')
            return redirect('logout/')
        else:
            print ('Nikal bsdk')
        
    else: 
        return render(request,'login.html')

def logout(request):
    return render(request,'logout.html')