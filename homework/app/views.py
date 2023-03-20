from django.shortcuts import render,redirect
from .models import homework
from .forms import addform
from django.http import FileResponse
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def homepage(request):
    return render(request,'index.html',{})

def loginuser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'username or password is incorrect!')
    return render(request,'login.html',{})

def logoutuser(request):
    logout(request)
    return redirect('/')

@login_required(login_url='login')
def add(request):
    form=addform()
    if request.method == 'POST':
        form=addform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/addwork')
    return render(request,'add.html',{'form':form})

def update(request,id):
    addmodel=homework.objects.get(id=id)
    form=addform(instance=addmodel)
    if request.method=="POST":
        form=addform(request.POST,instance=addmodel)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'update.html',{'form':form})

def first(request):
    model=homework.objects.filter(Q(Semester='1'))
    return render(request,'1.html',{'model':model})

def second(request):
    model=homework.objects.filter(Q(Semester='2'))
    return render(request,'2.html',{'model':model})

def third(request):
    model=homework.objects.filter(Q(Semester='3'))
    return render(request,'3.html',{'model':model})

def fourth(request):
    model=homework.objects.filter(Q(Semester='4'))
    return render(request,'4.html',{'model':model})

def fifth(request):
    model=homework.objects.filter(Q(Semester='5'))
    return render(request,'5.html',{'model':model})

def sixth(request):
    model=homework.objects.filter(Q(Semester='6'))
    return render(request,'6.html',{'model':model})

def seventh(request):
    model=homework.objects.filter(Q(Semester='7'))
    return render(request,'7.html',{'model':model})

def eighth(request):
    model=homework.objects.filter(Q(Semester='8'))
    return render(request,'8.html',{'model':model})