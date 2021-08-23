from django.urls import path

from todos_app.todos.views import index, create_todo, delete_todo, update_todo

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_todo, name='create_todo'),
    path('delete/<int:pk>', delete_todo, name='delete_todo'),
    path('update/<int:pk>', update_todo, name='update_todo'),
]