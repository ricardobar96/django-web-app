from django.urls import path
from .views import ListToDo, DetailTask

urlpatterns = [path('', ListToDo.as_view(), name='toDo'),
               path('task/<int:pk>', DetailTask.as_view(), name='task')]