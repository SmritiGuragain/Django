from django.shortcuts import render,redirect
from .forms import addform
from .models import info
from django.db.models import Q

# Create your views here.
def home(request):
    modela=info.objects.all()
    return render(request,'index.html',{'modela':modela})

def add(request):
    model=addform()
    if request.method=="POST":
        form=addform(request.POST,request.FILES)
        form.save()
        return redirect("/");
    return render(request,'add.html',{'model':model})

def describe(request,id):
    modulo=info.objects.get(id=id)
    return render(request,'describe.html',{'modulo':modulo})

def certificate(request):
    model=info.objects.filter(Q(Category='Certificate'))
    return render(request,'show.html',{'model':model})

def cat(request):
    model=info.objects.filter(Q(Category="Cat"))
    return render(request,'show.html',{'model':model})

def delete(request,id):
    modelo=info.objects.get(id=id)
    modelo.delete()
    return redirect("/")

def update(request,id):
    model=info.objects.get(id=id)
    formo=addform(instance=model)
    if request.method=="POST":
        formo=addform(request.POST,request.FILES,instance=model)
        if formo.is_valid():
            formo.save()
            return redirect('/')
    return render(request,'update.html',{'formo':formo})