from django.views.generic import ListView
from todo.models import Todo

# Create your views here.

class ToDoList(ListView):
    template_name = "todo/landing.html"
    model = Todo

