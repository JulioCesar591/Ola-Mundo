from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from .models import Todo

from .forms import TodoForm


class TodoListView(ListView):
    model = Todo
    context_object_name = "alunos_list"


class TodoCreateView(CreateView):
    model = Todo
    context_object_name = "alunos_list"
    form_class = TodoForm
    success_url = reverse_lazy("todo_list")


class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy("todo_list")


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")


class TodoCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.mark_complete()
        return redirect("todo_list")


class TodoReopenView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.finished = None
        todo.save()
        return redirect("todo_list")
