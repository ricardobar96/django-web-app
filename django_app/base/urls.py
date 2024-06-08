from django.urls import path
from .views import ListToDo

urlpatterns = [path('', ListToDo.as_view(), name='To Do')]