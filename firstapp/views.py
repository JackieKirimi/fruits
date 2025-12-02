from django.shortcuts import render ,get_object_or_404, redirect
from django.http import HttpResponse
from .models import Fruit
from .forms import FruitForm

# Create your views here.
def fruitGarden(request):
    return HttpResponse("Welcome to my fruit garden")

def home(request):
    return redirect('fetchAll')

def createFruit(request):
    form=FruitForm()
    if request.method=="POST":
        form=FruitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("fetchAll")
    
    context={"form":form}
    return render(request, "forms.html",context)

def fetchAllFruits(request):
    fruits=Fruit.objects.all()
    context={"fruits":fruits}
    return render (request,"fruit.html",context)

def fruitDetail(request,id):
    fruit=get_object_or_404(Fruit,pk=id)
    context={"fruit":fruit}
    return render(request,'fruit_details.html',context)

def updateFruit(request,id):
    fruit=get_object_or_404(Fruit,pk=id)
    form=FruitForm(instance=fruit)
    if request.method=="POST":
        form=FruitForm(request.POST,instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('fetchAll')
    return render(request,'forms.html',{'form':form})

def deleteFruit(request,id):
    fruit=get_object_or_404(Fruit,pk=id)
    if request.method=="POST":
        fruit.delete()
        return redirect('fetchAll')
    context={"fruit":fruit}
    return render(request,'fruit_confirm_delete.html',{'fruit':fruit})