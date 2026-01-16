
from django.shortcuts import render
from django.http import HttpResponse
from todos.models import Task


def home(request):
      tasks = Task.objects.filter(is_completed=False).order_by('-created_at')
      context = {
            'tasks': tasks,
            }

      return render(request, 'home.html', context )
      

    #  return HttpResponse("<h1>Hello, welcome to the ToDo app! </h1>")    # return render(request, 'todo_main/home.html')   
