from django.urls import path
from . import views

app_name = 'first'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('<int:pk>/<slug:article_slug>/', views.DetailTodo.as_view(), name='detail_todo')
]