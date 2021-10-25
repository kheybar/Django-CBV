from django.urls import reverse_lazy
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.views.generic.edit import FormMixin
from django.views.generic.dates import MonthArchiveView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify
from django.contrib import messages
from .models import Todo, Comment
from .forms import CommentForm


class Home(ListView):
    template_name = 'first/home.html'
    model = Todo
    context_object_name = 'todos'
    ordering = ['-created']



class DetailTodo(LoginRequiredMixin, FormMixin, DetailView):
    template_name = 'first/detail.html'
    # model = Todo
    context_object_name = 'todo'
    # slug_field = 'slug'
    # slug_url_kwarg = 'article_slug'

    def get_queryset(self, **kwargs):
        return Todo.objects.filter(id=self.kwargs['pk'], slug__iexact=self.kwargs['todo_slug'])
    

    # FormMixin
    form_class = CommentForm

    def get_success_url(self):
        return reverse('first:detail_todo', kwargs={'pk': self.object.pk, 'todo_slug': self.object.slug})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object() # اون آبجکتی که کاربر داره براش فرم پر میکنه
        form = self.get_form() # برای دریافت فرم پر شده توسط کاربر از این متود استفاده میکنیم
        if form.is_valid():
            cd = form.cleaned_data
            create_comment = Comment(todo=self.object, name=cd['name'], body=cd['body'])
            create_comment.save()
            messages.success(request=request, message='your todo comment successfully', extra_tags='success')
        return super().form_valid(form)



class CreateTodo(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ('title',)
    template_name = 'first/create.html'
    success_url = reverse_lazy('first:home')

    def form_valid(self, form):
        todo = form.save(commit=False)
        todo.slug = slugify(form.cleaned_data['title'])
        todo.save()
        messages.success(self.request, 'your todo add successfully', extra_tags='success')
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