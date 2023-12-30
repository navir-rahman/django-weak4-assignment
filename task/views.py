from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import TaskModel
from .forms import TaskForm

def add_task(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('add_task')
    else:
        task_form = TaskForm()
    return render(request, 'task_form.html', {'form': task_form})

def edit_task(request, id):
    task= TaskModel.objects.get(pk=id)
    task_form = TaskForm(instance=task)
    # print(task)
    if request.method == 'POST':
        task_form = TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('home')
    return render(request, 'task_form.html', {'form': task_form})

def delete_task(request, id):
    task = TaskModel.objects.get(pk=id)
    task.delete()
    return redirect('home')
