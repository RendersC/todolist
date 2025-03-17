from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import TodoList
from django.urls import reverse_lazy


def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')


class TodoListView(LoginRequiredMixin, ListView):
    model = TodoList
    template_name = 'main/home.html'
    context_object_name = 'todos'

    def get_queryset(self):
        return TodoList.objects.filter(user=self.request.user)


class TodoUpdateView(LoginRequiredMixin,UpdateView):
    model = TodoList
    fields = ['title']
    template_name = 'main/todo_edit.html'
    success_url = reverse_lazy('home')


class TodoDeleteView(LoginRequiredMixin,DeleteView):
    model = TodoList
    template_name = 'main/todo_delete.html'
    success_url = reverse_lazy('home')


class TodoCreateView(LoginRequiredMixin,CreateView):
    model = TodoList
    fields = ['title']
    template_name ='main/todo_create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

