from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from kjpage.models import Student
from django.contrib import messages
import datetime
import re
# Create your views here.
def register(request):
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        first_name=request.POST["first"]
        last_name=request.POST["last"]
        phone=request.POST["phone"]
        
        user=User.objects.create_user(username,email,password=password,first_name=first_name,last_name=last_name)
        user.save()
        s=Student(user=user)
        s.phone=phone
        
        s.save()

        messages.info(request,"Please login by clicking the login button at bottom right of page")
        return render(request,"home.html")

def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            request.session['timer'] = (datetime.datetime.now()+datetime.timedelta(minutes=60)).strftime("%d-%b-%Y (%H:%M:%S)")





            
            
            
            print("//////////////////")
            print(request.session["timer"])
            # x=re.split("^([0-9]{2})-([a-zA-Z]{3})-([0-9]{4})\s\(([0-9]{2}):([0-9]{2}):([0-9]{2})\)$",request.session["timer"])
            # for i in x:
            #     print(i)
            print("##################")
            return redirect("code")
        else:
            messages.info(request,"incorrect credintials")
            return redirect("/")
    else:
        return redirect("home")

def logout(request):
    auth.logout(request)
    return redirect("/")