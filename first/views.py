from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import (
    ListView, DetailView, FormView
    )
from .models import Todo
from .forms import TodoCreateForm



class Home(ListView):
    template_name = 'first/home.html'
    model = Todo
    context_object_name = 'todos'
    ordering = ['-created']



class DetailTodo(DetailView):
    template_name = 'first/detail.html'
    model = Todo
    context_object_name = 'todo'
    slug_field = 'slug'
    slug_url_kwarg = 'article_slug'

    def get_queryset(self, **kwargs):
        return Todo.objects.filter(id=self.kwargs['pk'], slug__iexact=self.kwargs['article_slug'])



class TodoCreate(FormView):
    form_class = TodoCreateForm
    template_name = 'first/todo_create.html'
    success_url = reverse_lazy('first:home')

    def form_valid(self, form):
        self.create_todo(form.cleaned_data)
        return super().form_valid(form)

    def create_todo(self, data):
        todo = Todo(title=data['title'], slug=slugify(data['title']))
        todo.save()










