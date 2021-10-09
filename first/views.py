from django.views.generic.list import ListView

from .models import Todo


class Home(ListView):
    template_name = 'first/home.html' # default 'app_name/modelname_list.html'
    context_object_name = 'todos' # default object_list

    # queryset = Todo.objects.filter() # good for normal query
    # model = Todo # for get all objects from model
    def get_queryset(self):
        return Todo.objects.all().order_by('-created')
    
    # ordering = ['-created']
    # paginated_by = 9


