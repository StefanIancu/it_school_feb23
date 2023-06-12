from django.views.generic import ListView, DetailView
from todo.models import Todo
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class ToDoList(LoginRequiredMixin ,ListView):
    template_name = "todo/landing.html"
    model = Todo

class ViewOne(LoginRequiredMixin ,DetailView):
    template_name = "todo/detail.html"
    model = Todo

