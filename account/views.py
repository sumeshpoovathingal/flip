from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

def register(request):
    if request.method=='POST':
        # name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request,"username already taken register with another username")
            return render(request,'register.html')
        else :
            user = User.objects.create_user( username=username, email=email, password=password)
            user.save();
            print("user created")
            return render(request,'login.html')
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password= request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid username or password')
            return render(request,'login.html')
    else:

        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')