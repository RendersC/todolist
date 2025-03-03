from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import TodoList
from django.urls import reverse_lazy


def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')


class TodoListView(ListView):
    model = TodoList
    template_name = 'main/home.html'
    context_object_name = 'todos'


class TodoUpdateView(UpdateView):
    model = TodoList
    fields = ['title']
    template_name = 'main/todo_edit.html'
    success_url = reverse_lazy('home')


class TodoDeleteView(DeleteView):
    model = TodoList
    template_name = 'main/todo_delete.html'
    success_url = reverse_lazy('home')


class TodoCreateView(CreateView):
    model = TodoList
    fields = ['title']
    template_name ='main/todo_create.html'
    success_url = reverse_lazy('home')
