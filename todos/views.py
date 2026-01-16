from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task


# Create your views here.
def addTask(request):
    taskdata = request.POST['task']
    Task.objects.create(task=taskdata)

    # return render(request, 'todos/addTask.html')
    return redirect('home')
