from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


class LoginUser(auth_views.LoginView):
    template_name = 'accounts/login.html'
    # extra_context = {'name': 'mahdi'}


class LogoutUser(auth_views.LogoutView):
    next_page = 'first:home'


class UserPassReset(auth_views.PasswordResetView):
    template_name = 'accounts/password_reset_form.html' # صفحه ای که کاربر قراره بیاد و ایمیلشو وارد کنه
    success_url = reverse_lazy('accounts:password_reset_done')
    email_template_name = 'accounts/password_reset_email.html' # متنی که قراره به کاربر ایمیل بشه



class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'



class PasswordResetConfirmViewView(auth_views.PasswordResetConfirmViewView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')



class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'