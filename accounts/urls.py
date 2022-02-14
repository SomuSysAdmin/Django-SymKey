from django.urls import path

from accounts.views import AccLoginView, AccLogoutView

urlpatterns = [
    path('login/', AccLoginView.as_view(), name='login'),
    path('logout/', AccLogoutView.as_view(), name='logout'),
]

