from django.urls import path
from todo.views import ToDoList, ViewOne

urlpatterns = [
    path('', ToDoList.as_view(), name="todo_list"),
    path('<int:pk>', ViewOne.as_view(), name="todo_one"),
]
