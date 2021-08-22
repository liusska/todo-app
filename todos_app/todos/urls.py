from django.urls import path

from todos_app.todos.views import index, create_todo, delete_todo, change_todo_state

urlpatterns = [
    path('', index),
    path('todos-add/', create_todo),
    path('todos-delete/<int:pk>', delete_todo),
    path('todos-change-state/<int:pk>', change_todo_state),
]