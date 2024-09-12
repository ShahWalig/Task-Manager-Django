from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Tasks
from .forms import TaskForm


def index(request):
    form = TaskForm()
    task = Tasks.objects.all().order_by('-id')
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'tasks': task,
        'TaskForm': form,
    }
    return render(request, 'tasks.html', context)


def updateTask(request, pk):
    task = Tasks.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')

    context = {
        'TaskForm': form,

    }
    return render(request, 'update-task.html', context)


def deleteTask(request, pk):
    task = Tasks.objects.get(id=pk)
    if request.method == "POST":
        task.delete()
        return redirect('/')

    context = {"task": task}
    return render(request, 'delete-task.html', context)
