from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from . import models

def homepage(request):
    comp_tasks = models.Task.objects.filter(is_comp=True).order_by('-updated_ts')
    uncomp_tasks = models.Task.objects.filter(is_comp=False).order_by('-updated_ts')
    data={'comp_tasks': comp_tasks, 'uncomp_tasks': uncomp_tasks}
    return render(request, "home.html", data)

def addTask(request):
    if request.method=='POST':
        task = request.POST['task']
        obj = models.Task.objects.create(task=task)
        obj.save()
    else:
        return redirect('home')
    return redirect('home')

def markAsDone(request, pk):
    # task = models.Task.objects.get(id=pk)
    task=get_object_or_404(models.Task, id=pk)
    task.is_comp=True
    task.save()
    return redirect('home')

def markAsUndone(request, pk):
    # task = models.Task.objects.get(id=pk)
    task=get_object_or_404(models.Task, id=pk)
    task.is_comp=False
    task.save()
    return redirect('home')

def deleteTask(request, pk):
    # task = models.Task.objects.get(id=pk)
    task=get_object_or_404(models.Task, id=pk)
    task.delete()
    return redirect('home')

def updateTask(request, pk):
    # task = models.Task.objects.get(id=pk)
    task=get_object_or_404(models.Task, id=pk)
    if request.method=='POST':
        task.task=request.POST['task']
        task.save()
        return redirect('home')
    return render(request, "update.html", {'task': task})