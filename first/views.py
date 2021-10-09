from django.views.generic.base import TemplateView
from .models import Todo


class Home(TemplateView):
    template_name = 'first/home.html'

    # todos = Todo.objects.all() # no class Atribute

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todos'] = Todo.objects.all() # Correct
        return context