from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import donerModel
from .forms import addForm

# Create your views here.
def homepage(request):
    model = donerModel.objects.all()
    return render(request,'index.html',{'model':model})

def add(request):
    form = addForm()
    if request.method=='POST':
        form=addForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/add')
    return render(request,'add.html',{'form':form})

def delete(request,id):
    modela = donerModel.objects.get(id=id)
    modela.delete()
    return redirect('/')

def update(request,id):
    addmodel=donerModel.objects.get(id=id)
    addforms=addForm(instance=addmodel)
    if request.method=='POST':
        addforms = addForm(request.POST,instance=addmodel)
        if addforms.is_valid():
            addforms.save()
            return redirect('/add')
    return render(request,'update.html',{'addforms':addforms})