from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

tasks = ['Task 1', 'Task 2', 'Task 3']

class TaskForm(forms.Form):
    task = forms.CharField(label='Task', max_length=100)
    priority = forms.IntegerField(label='Priority', min_value=1, max_value=10)

def index(request):
    return render(request, 'tasks/index.html', {
        'tasks': tasks
    })

def add(request):
    return render(request, 'tasks/add.html')

def add2(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            tasks.append(task)
            return HttpResponseRedirect(reverse('tasks:index'))
        else:
            return render(request, 'tasks/add2.html', {
                'form': form
            })
    else:
        return render(request, 'tasks/add2.html', {
            'form': TaskForm()
        })