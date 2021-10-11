from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Todo


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


