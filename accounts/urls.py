from django.urls import path
# from django.contrib.auth import views as auth_views
from . import views


app_name = 'accounts'
urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login')
    path('login/', views.LoginUser.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', views.LogoutUser.as_view(), name='logout'),
    path('reset/', views.UserPassReset.as_view(), name='reset_pass'),

]