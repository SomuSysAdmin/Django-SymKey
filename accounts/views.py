from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView


class AccLoginView(LoginView):
    template_name = 'accounts/login.html'
    
class AccLogoutView(LogoutView):
    template_name = 'accounts/logout.html'