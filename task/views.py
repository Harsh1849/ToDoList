from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def home(request):
    tasks = Task.objects.all()
    forms = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {'tasks':tasks , 'forms':forms}
    return render(request,'task/home.html',context)

def updatetask(request , pk):
    task = Task.objects.get(id = pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST , instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {'form':form }
    
    return render(request , 'task/update_task.html' ,context)

def deletetask(request , pk):
    task = Task.objects.get(id = pk)

    if request.method == 'POST':
        form = TaskForm(request.POST , instance=task)
        task.delete()
        return redirect("/")

    context = {'task':task }
    
    return render(request , 'task/delete_task.html', context)
