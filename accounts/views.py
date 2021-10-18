from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views



class LoginUser(auth_views.LoginView):
    template_name = 'accounts/login.html'
    # extra_context = {'name': 'mahdi'}