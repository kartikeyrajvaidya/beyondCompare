from django.shortcuts import render
from django.urls import resolve,reverse_lazy
from django.views.generic import (TemplateView,ListView,
                                    DetailView,CreateView,
                                    UpdateView,DeleteView)

from . import forms

class SingUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login/')
    template_name = 'accounts/signup.html'
