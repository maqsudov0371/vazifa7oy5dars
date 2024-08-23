from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView

class HomePageView(ListView):
    model = Podca
    template_name = 'index.html'
    context_object_name = 'podca'


class HomeView(ListView):
    model = Musican
    template_name = 'home.html'