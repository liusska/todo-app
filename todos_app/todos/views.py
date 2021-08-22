from django.shortcuts import render, redirect

from todos_app.todos.models.todo import Todo
from todos_app.todos.models.todo import Person
from todos_app.todos.forms import CreateTodoFrom


def index(request):
    context = {
        'todos': Todo.objects.all(),
        'form': CreateTodoFrom()
    }
    return render(request, 'index.html', context)


def create_todo(request):
    form = CreateTodoFrom(request.POST)

    if form.is_valid():
        text = form.cleaned_data['text']
        description = form.cleaned_data['description']
        todo = Todo(
            text=text,
            description=description,
            # owner=owner
        )
        todo.save()
        return redirect('/')
    context = {
        'todos': Todo.objects.all(),
        'form': form,
    }
    return render(request, 'index.html', context)


def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('/')


def change_todo_state(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.state = not todo.state
    todo.save()
    return redirect('/')
