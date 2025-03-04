from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Task
from .forms import TaskForm


def home_todolist(request):
    """Create task and return homepage with todolist"""
    if request.user.is_authenticated:
        all_tasks = Task.objects.filter(author=request.user)
        if request.method == "POST":
            form = TaskForm(request.POST or None)
            if form.is_valid():
                task = form.save(commit=False)
                task.author = request.user
                task.save()
                messages.success(request, 'Task has been added to list!')
    else:
        all_tasks = None
    return render(request, 'todolist/todolist.html', {'all_tasks': all_tasks})


def delete_task(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)
    task.delete()
    messages.success(request, 'Task has been deleted!')
    return redirect('home_todolist')


def cross_off_task(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)
    task.completed = True
    task.save()
    return redirect('home_todolist')


def uncross_task(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)
    task.completed = False
    task.save()
    return redirect('home_todolist')


def edit_task(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)
    if request.method == "POST":
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            form.save()
            return redirect('home_todolist')
    else:
        return render(request, 'todolist/edit.html', {'task': task})


def about_page(request):
    return render(request, 'todolist/about.html')
