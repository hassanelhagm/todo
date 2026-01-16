from django.contrib import admin
from django.urls import path, include
from  . import views

urlpatterns = [
   
    path('addTask', views.addTask, name='addTaskname' ),
    path('mark_as_done/<int:pk>', views.mark_as_done, name='mark_as_done_name' ),
    path('mark_as_undone/<int:pk>', views.mark_as_undone, name='mark_as_undone_name' ),
    path('edit_task/<int:pk>', views.edit_task, name='edit_task_name' ),
     path('delete_task/<int:pk>', views.delete_task, name='delete_task_name' ),
 
]
