from django.urls import path
from .views import ListToDo, DetailTask, CreateTask, UpdateTask, DeleteTask

urlpatterns = [path('', ListToDo.as_view(), name='tasks'),
               path('task/<int:pk>', DetailTask.as_view(), name='task'),
               path('create-task/', CreateTask.as_view(), name='create-task'),
               path('update-task/<int:pk>', UpdateTask.as_view(), name='update-task'),
               path('delete-task/<int:pk>', DeleteTask.as_view(), name='delete-task')]