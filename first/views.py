from django.shortcuts import render
from django.views import View


class Home(View):
    
    def get(self, request, *args, **kwargs):
        context = {
            'name': 'BOSS',
        }
        return render(request=request, template_name='first/home.html', context=context)

