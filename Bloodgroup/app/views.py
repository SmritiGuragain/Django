from django.shortcuts import render,redirect
from .models import doner
from .forms import addform,userform
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
# Create your views here.

@login_required(login_url='/')
@never_cache
def home(request):
    model=doner.objects.all()
    modela=addform()
    if request.method=="POST":
        form=addform(request.POST)
        form.save()
        return redirect("/home")
    return render(request,'index.html',{'model':model,'modela':modela})


def see(request,cat):
    model=doner.objects.filter(Q(Category=cat))
    modela=addform()
    if request.method=="POST":
        form=addform(request.POST)
        form.save()
        return redirect("/home")
    return render(request,'index.html',{'model':model,'modela':modela})


def delete(request,id):
    model=doner.objects.get(id=id)
    model.delete()
    return redirect("/home")



def update(request,id):
    modelo=doner.objects.get(id=id)
    model=doner.objects.all()
    modela=addform(instance=modelo)
    if request.method=="POST":
        form=addform(request.POST,instance=modelo)
        form.save()
        return redirect("/home")
    return render(request,'index.html',{'model':model,'modela':modela})

def search(request):
    var=request.GET.get('query')
    model=doner.objects.filter(Q(Name__icontains=var))
    return render(request,'search.html',{'model':model})


def loginuser(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/home')
        else:
            messages.info(request,'username or password is incorrect!')
    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect('/')


def check(request):
    x=doner.objects.all()
    model=[y for y in x if y.availability()=="Available"]
    modela=addform()
    if request.method=="POST":
        form=addform(request.POST)
        form.save()
        return redirect("/home")
    return render(request,'index.html',{'model':model,'modela':modela})


def signup(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        form=userform()
        if request.method=='POST':
            form=userform(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')

    return render(request,'signup.html',{'form':form})
