from django.shortcuts import render,redirect
from django.contrib.auth.models import User
import json
from django.http import JsonResponse
from django.contrib import auth
from django.urls import reverse
from django.contrib import messages
from django.views import View


# Create your views here.

class Registration(View):
    def get(self,request):
        return render(request, 'Authentication/registration.html')
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']

        if not User.objects.filter(username=username).exists():
            if len(password) < 6:
                messages.error(request, 'the password is too short')
                return render(request, 'Authentication/registration.html')
            user = User.objects.create_user(username=username)
            user.set_password(password)
            user.save()
            messages.success(request,"Account successfully created")
            return render(request,'Authentication/registration.html')
        return render(request,'Authentication/registration.html')




class Login(View):
    def get(self,request):
        return render(request,'Authentication/login.html')
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = auth.authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    auth.login(request,user)
                    return redirect('home')
                
            messages.success(request,'Invalid credentials, Try Again')
            return render(request,'Authentication/login.html')
        
        messages.success(request,"please fill all fields ")
        return render(request,'Authentication/login.html')

