
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
      return render(request, 'home.html')
    #  return HttpResponse("<h1>Hello, welcome to the ToDo app! </h1>")
    # return render(request, 'todo_main/home.html')   
