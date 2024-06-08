from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Task


class Login(LoginView):
    template_name = "base/login.html"
    field = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

class  ListToDo(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

class  DetailTask(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'

class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class UpdateTask(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')