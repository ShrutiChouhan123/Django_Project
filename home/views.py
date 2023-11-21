from django.shortcuts import render
from .models import Student
from django.contrib.auth.models import User
from django.contrib import auth



# Create your views here.
def index(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        users=User.objects.create_user(username=username,email=email,password=password)
        users.save()  
        return render(request,'login.html')
          
    else:
        return render(request,'index.html')

def addstudent(request):
    if(request.method=='POST'):
        obj=Student()
        obj.name=request.POST['name']
        obj.address=request.POST['address']
        obj.email=request.POST['email']
        obj.save()
        return render(request,'index.html')
    else:
        return render(request,'addstudent.html')

def showstudent(request):
    data=Student.objects.all()
    return render(request,'showstudent.html',{'data':data})

def login_page(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        users=auth.authenticate(username=username,password=password)
        if users is not None:
            auth.login(request,users)
            return redirect('addstudent.html')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')


    

