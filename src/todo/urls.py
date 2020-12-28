from django.urls import path
from .views import home, todo_add, todo_delete, todo_list, todo_update
urlpatterns = [
    path("", home, name="home"),
    path("list/", todo_list, name="todo-list"),
    path("add/", todo_add, name="todo-add"),
    path("<int:id>/update/", todo_update, name="todo-update"),
    path("<int:id>/delete", todo_delete, name="todo-delete")
]