from django.urls import path
from .views import ListToDo, DetailTask, CreateTask, UpdateTask, DeleteTask, Login
from django.contrib.auth.views import LogoutView

urlpatterns = [path('', ListToDo.as_view(), name='tasks'),
               path('login/', Login.as_view(), name='login'),
               path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
               path('task/<int:pk>', DetailTask.as_view(), name='task'),
               path('create-task/', CreateTask.as_view(), name='create-task'),
               path('update-task/<int:pk>', UpdateTask.as_view(), name='update-task'),
               path('delete-task/<int:pk>', DeleteTask.as_view(), name='delete-task'),]