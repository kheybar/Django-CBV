from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.views.generic.dates import MonthArchiveView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify
from django.contrib import messages
from .models import Todo


class Home(ListView):
    template_name = 'first/home.html'
    model = Todo
    context_object_name = 'todos'
    ordering = ['-created']



class DetailTodo(LoginRequiredMixin, DetailView):
    template_name = 'first/detail.html'
    # model = Todo
    context_object_name = 'todo'
    # slug_field = 'slug'
    # slug_url_kwarg = 'article_slug'

    def get_queryset(self, **kwargs):
        return Todo.objects.filter(id=self.kwargs['pk'], slug__iexact=self.kwargs['article_slug'])



class CreateTodo(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ('title',)
    template_name = 'first/create.html'
    success_url = reverse_lazy('first:home')

    def form_valid(self, form):
        todo = form.save(commit=False)
        todo.slug = slugify(form.cleaned_data['title'])
        todo.save()
        messages.success(self.request, 'your todo add successfully.', extra_tags='success')
        return super().form_valid(form)



class DeleteTodo(LoginRequiredMixin, DeleteView):
    model = Todo
    template_name = 'first/delete.html'
    success_url = reverse_lazy('first:home')


class UpdateTodo(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = ('title',)
    template_name = 'first/update.html'
    success_url = reverse_lazy('first:home')

    def form_valid(self, form):
        todo = form.save(commit=False)
        todo.slug = slugify(form.cleaned_data['title'])
        todo.save()
        messages.success(self.request, 'your todo update successfully.', extra_tags='success')
        return super().form_valid(form)



class MonthTodo(MonthArchiveView):
    model = Todo
    date_field = 'published'
    month_format = '%m'
    template_name = 'first/todo_month.html'
    context_object_name = 'todos'