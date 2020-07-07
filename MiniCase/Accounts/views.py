from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

def register(request):
    
    if request.method == 'POST':
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username is taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email is taken')
                return redirect('register')
            else:
                # Create a user and default them to inactive
                user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name, is_active=False)
                user.save()
        else:
            messages.info(request,'Passwords do not match')
            return redirect('register')
        return redirect('/')
    else: 
        return render(request,'MiniCaseApp/register.html')