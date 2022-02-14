from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .models import Credential
from .forms import CredsCreateForm


class RequestorIsUserMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        if self.request.user == obj.user: 
            return True
        return False

class CredsListView(LoginRequiredMixin, ListView):
    model = Credential
    template_name = "keystore/home.html"
    
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class CredsDetailView(LoginRequiredMixin, RequestorIsUserMixin, DetailView):
    model = Credential
    template_name = "keystore/detail.html"


class CredsCreateView(LoginRequiredMixin, CreateView):
    model = Credential
    form_class = CredsCreateForm
    template_name = "keystore/add.html"
    
    def form_valid(self, form):
        # set the creator of the instance to the currently logged in user
        form.instance.user = self.request.user
        return super().form_valid(form)


class CredsUpdateView(LoginRequiredMixin, RequestorIsUserMixin, UpdateView):
    model = Credential
    form_class = CredsCreateForm
    template_name = "keystore/edit.html"


class CredsDeleteView(LoginRequiredMixin, RequestorIsUserMixin, DeleteView):
    model = Credential
    template_name = "keystore/delete.html"
    success_url = reverse_lazy('creds-home')