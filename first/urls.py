from django.urls import path
from . import views

from django.views.generic.base import TemplateView # with out write class

app_name = 'first'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('', TemplateView.as_view(template_name='first/home.html'), name='home'), # good for static page
]